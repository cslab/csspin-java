# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2020 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the mvn plugin for cs.spin"""

import os
import random
import sys
import tarfile
import urllib

from spin import Verbosity, config, exists, option, setenv, sh, task, warn

defaults = config(
    exe="mvn",
    version="3.8.3",
    pom_file="pom.xml",
    mirrors=[
        "https://ftp.fau.de/apache/",
        "https://dlcdn.apache.org/",
    ],
    url="maven/maven-3/{mvn.version}/binaries/apache-maven-{mvn.version}-bin.tar.gz",
    mavendir="{spin.data}/apache-maven-{mvn.version}",
    requires=config(spin=["spin_java.java"]),
)


def provision(cfg):
    """Provision the mvn plugin"""
    if not exists(cfg.mvn.mavendir):

        from path import Path
        from spin import download

        random.shuffle(cfg.mvn.mirrors)
        zipfile = cfg.mvn.mavendir / Path(cfg.mvn.url).basename()

        for mirror in cfg.mvn.mirrors:
            try:
                download(mirror + cfg.mvn.url, zipfile)
            except urllib.error.HTTPError as e:
                # maven removes old version from the mirrors...
                if e.status == 404:
                    warn(
                        f"Maven {cfg.mvn.version} not found in the mirrors... "
                        f"Trying to retrieve version {cfg.mvn.version} from archive."
                    )
                    download(f"https://archive.apache.org/dist/{cfg.mvn.url}", zipfile)
                else:
                    raise
            except urllib.error.URLError:
                warn(f"Mirror {mirror} currently not reachable...")
                continue
            break
        else:
            raise Exception(  # pylint: disable=broad-exception-raised
                "Currently no mirror reachable"
            )
        with tarfile.open(zipfile, "r:gz") as tar:
            tar.extractall(cfg.mvn.mavendir.dirname())  # nosec: B202
        zipfile.unlink()


def init(cfg):
    """Initialize the mvn plugin"""
    bindir = (cfg.mvn.mavendir / "bin").normpath()
    setenv(
        f"set PATH={bindir}{os.pathsep}$PATH",
        PATH=os.pathsep.join((f"{bindir}", "{PATH}")),
    )


@task(when="build")
def mvn(
    cfg,
    pom_file: option(
        "-f",  # noqa: F821
        "--file",  # noqa: F821
        "pom_file",  # noqa: F821
        show_default=(
            "Force the use of an alternate POM file "  # noqa: F722
            "(or directory with pom.xml)"
        ),
    ),
    defines: option(
        "-D",  # noqa: F821
        "--define",  # noqa: F821
        "defines",  # noqa: F821
        multiple=True,
        show_default="Define a system property",  # noqa
    ),
    args,
):
    """Run maven command"""
    cmd = "{mvn.exe}"
    if sys.platform.startswith("win32"):
        cmd += ".cmd"
    opts = cfg.mvn.opts
    if cfg.verbosity == Verbosity.QUIET:
        opts.append("-q")
    # add pom file
    opts.append("-f")
    opts.append(pom_file or cfg.mvn.pom_file)

    # add defines
    cfg_defines = cfg.mvn.defines
    for d in defines:
        name, val = d.split("=")
        cfg_defines[name] = val

    for d in cfg_defines.items():
        opts.append(f"-D{d[0]}={d[1]}")

    # do not use goals when some extra args are used
    if not args:
        opts.extend(cfg.mvn.goals)
    sh(cmd, *opts, *args)
