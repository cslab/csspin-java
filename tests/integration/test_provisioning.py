# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for spin_java"""


import shlex
import shutil
import subprocess

import pytest
from path import Path

JAVA_EXISTS = shutil.which("java")


def execute_spin(yaml, env, path="tests/integration/yamls", cmd=""):
    """Helper function to execute spin and return the output"""
    try:
        return subprocess.check_output(
            shlex.split(
                f"spin -p spin.data={env} -C {path} --env {str(env)} -f {yaml} " + cmd
            ),
            encoding="utf-8",
            stderr=subprocess.PIPE,
        ).strip()
    except subprocess.CalledProcessError as ex:
        print(ex.stdout)
        print(ex.stderr)
        raise


@pytest.mark.integration()
def test_java_provision(tmp_path):
    """Provision the java plugin"""
    yaml = "java.yaml"
    execute_spin(yaml=yaml, env=tmp_path, cmd="cleanup")
    execute_spin(yaml=yaml, env=tmp_path, cmd="provision")
    execute_spin(yaml=yaml, env=tmp_path, cmd="run java --version")


@pytest.mark.integration()
@pytest.mark.skipif(not JAVA_EXISTS, reason="java not installed.")
def test_java_use_provision(tmp_path):
    """Provision the java plugin but using a local java installation"""
    yaml = "java.yaml"

    execute_spin(yaml=yaml, env=tmp_path, cmd="cleanup")
    provision_log = execute_spin(
        yaml=yaml,
        env=tmp_path,
        cmd="-p java.use=java provision",
    )
    version_log = execute_spin(
        yaml=yaml,
        env=tmp_path,
        cmd="-p java.use=java run java --version",
    )

    expected_java_home = (
        f"JAVA_HOME={Path(shutil.which('java')).realpath().dirname().dirname()}"
    )
    assert expected_java_home in provision_log
    assert expected_java_home in version_log


@pytest.mark.integration()
def test_mvn_provision(tmp_path):
    """Provision the mvn plugin"""
    yaml = "mvn.yaml"
    execute_spin(yaml=yaml, env=tmp_path, cmd="cleanup")
    execute_spin(yaml=yaml, env=tmp_path, cmd="provision")
    execute_spin(yaml=yaml, env=tmp_path, cmd="run mvn --version")
