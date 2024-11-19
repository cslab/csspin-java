# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Implementation of the java plugin for cs.spin"""

import os

from path import Path
from spin import config, die, echo, interpolate1, mv, setenv

defaults = config(install_dir="{spin.data}/java")


def set_environment(cfg):
    """Set the environment variables needed for java"""
    java_bin_dir = cfg.java.java_home / "bin"
    setenv(
        JAVA_HOME=cfg.java.java_home,
        PATH=os.pathsep.join((java_bin_dir, "{PATH}")),
    )


def configure(cfg):
    """Configure the java plugin"""
    if cfg.java.use:
        cfg.java.java_home = cfg.java.use
    elif cfg.java.version:
        cfg.java.java_home = Path(interpolate1(cfg.java.install_dir)) / str(
            cfg.java.version
        )
    else:
        die(
            "'spin_java.java' does not set a default version for java. "
            "Set either 'java.version' or 'java.use'."
        )


def provision(cfg):
    """Install java if it does not exist"""
    if not cfg.java.java_home.exists():
        from tempfile import TemporaryDirectory

        import jdk

        with TemporaryDirectory() as tmp_dir:
            echo(f"Downloading JDK from {jdk.get_download_url(cfg.java.version)}")
            jdk_path = jdk.install(cfg.java.version, path=Path(tmp_dir))
            mv(jdk_path, cfg.java.java_home)

    set_environment(cfg)


def init(cfg):
    """Initialize the environment"""
    set_environment(cfg)
