# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for spin_java"""

from os import getcwd
from os.path import join

import pytest
from spin import backtick, cd, cli


@pytest.fixture(autouse=True)
def cfg():
    """Fixture creating the configuration tree"""
    cwd = getcwd()
    cli.load_config_tree("tests/yamls/minimal.yaml")
    cd(cwd)


def execute_spin(tmpdir, what, cmd, path="tests/integration"):
    """Helper to execute spin calls via spin."""
    output = backtick(
        f"spin -p spin.data={tmpdir} -q -C {path} --env {tmpdir} -f"
        f" {what} --cleanup --provision {cmd}"
    )
    output = output.strip()
    return output


@pytest.mark.integration()
def test_java(tmpdir):
    """The java plugin-package can be provisioned"""
    output = execute_spin(
        tmpdir=tmpdir,
        what=join("tests", "integration", "yamls", "java.yaml"),
        cmd="run java --version",
    )
    assert "openjdk 19." in output
