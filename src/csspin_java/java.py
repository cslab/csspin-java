# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# https://www.contact-software.com/
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Implementation of the java plugin for csspin"""

import importlib
import os
import re
import shutil
import subprocess  # nosec: B404
import time
from tempfile import TemporaryDirectory
from urllib.parse import unquote

import requests
from csspin import config, die, echo, info, interpolate1, memoizer, mv, setenv, warn
from path import Path

defaults = config(install_dir="{spin.data}/java")

ONE_DAY = 24 * 60 * 60


def set_environment(cfg):
    """Set the environment variables needed for java"""
    java_bin_dir = cfg.java.java_home / "bin"
    setenv(
        JAVA_HOME=cfg.java.java_home,
        PATH=os.pathsep.join((java_bin_dir, "{PATH}")),
    )


def _needs_update(java_home, url):
    """Check whether the java behind ``url`` differs from the installed one.

    Both versions are extracted as ``<version>+<build>`` (e.g. ``25.0.5+8``)
    and compared as strings. The Adoptium URL only names the feature release
    and redirects to the release asset, so a HEAD request reads the version
    from the redirect instead of downloading anything. The request is made at
    most once per day.
    """
    version_re = r"\d+(?:\.\d+)*\+\d+"

    # java_home is specific to the configured version, so this limits the
    # requests to one per day and major version.
    with memoizer(java_home / "update_check.memo") as memo:
        timestamps = memo.items()
        if timestamps and time.time() - timestamps[-1] < ONE_DAY:
            return False

        info(f"Checking whether a newer java is available for {url}")
        try:
            result = subprocess.run(  # nosec: B603
                [java_home / "bin" / "java", "--version"],
                capture_output=True,
                check=True,
                encoding="utf-8",
            )
        except (OSError, subprocess.CalledProcessError):
            return True
        installed = re.search(version_re, result.stdout)
        if installed is None:
            return True

        try:
            response = requests.head(
                url,
                allow_redirects=False,
                timeout=10,
                # Cloudflare in front of api.adoptium.net rejects the default
                # user agent of some HTTP clients.
                headers={
                    "User-Agent": (
                        f"csspin-java/v{importlib.metadata.version('csspin-java')}"
                        " (https://github.com/cslab/csspin-java)"
                    )
                },
            )
            response.raise_for_status()
        except requests.RequestException as ex:
            # A failing lookup must not break a working installation.
            warn(f"Could not determine the latest java version: {ex}")
            return False

        location = response.headers.get("Location", "")

        memo.clear()
        memo.add(time.time())

    remote = re.search(version_re, unquote(location))
    return remote is not None and remote.group() != installed.group()


def configure(cfg):
    """Configure the java plugin"""
    if cfg.java.use:
        warn(f"java.version will be ignored, since java.use is set to '{cfg.java.use}'")
        if java_path := shutil.which(interpolate1(cfg.java.use)):
            # assuming java to be $JAVA_HOME/bin/java
            cfg.java.java_home = Path(java_path).realpath().dirname().dirname()
        else:
            die(f"Could not find java executable '{cfg.java.use}'")
    elif cfg.java.version:
        cfg.java.java_home = Path(interpolate1(cfg.java.install_dir)) / str(
            cfg.java.version
        )
    else:
        die(
            "'csspin_java.java' does not set a default version for java. "
            "Set either 'java.version' or 'java.use'."
        )


def provision(cfg):
    """Install java if it does not exist"""
    if cfg.java.version and not cfg.java.use:
        import jdk

        url = jdk.get_download_url(cfg.java.version)
        java_home = cfg.java.java_home
        if not java_home.exists() or _needs_update(java_home, url):
            with TemporaryDirectory() as tmp_dir:
                echo(f"Downloading JDK from {url}")
                jdk_path = jdk.install(cfg.java.version, path=Path(tmp_dir))
                # Remove the old installation only after the download
                # succeeded, so a failure leaves a working java behind.
                if java_home.exists():
                    shutil.rmtree(java_home)
                mv(jdk_path, java_home)

    set_environment(cfg)


def init(cfg):
    """Initialize the environment"""
    set_environment(cfg)
