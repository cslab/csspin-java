# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2026 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Unit tests for the version check of the java plugin"""

# The version check is intentionally private, as its behavior is only
# reachable through provision, which requires a network and a real install.
# pylint: disable=protected-access

import subprocess
import time
from unittest.mock import Mock

import pytest
import requests
from csspin import Memoizer, memoizer
from path import Path

from csspin_java import java

JAVA_VERSION_OUTPUT = """\
openjdk 25.0.5 2026-10-21 LTS
OpenJDK Runtime Environment Temurin-25.0.5+8 (build 25.0.5+8-LTS)
OpenJDK 64-Bit Server VM Temurin-25.0.5+8 (build 25.0.5+8-LTS, mixed mode)
"""
LOCATION = (
    "https://github.com/adoptium/temurin25-binaries/releases/download/"
    "jdk-{}/OpenJDK25U-jdk_x64_linux_hotspot.tar.gz"
)
URL = "https://example.com/latest"


@pytest.fixture(autouse=True)
def fixture_silent_info(monkeypatch):
    """``info`` needs an initialized csspin configuration"""
    monkeypatch.setattr(java, "info", lambda *_: None)


@pytest.fixture(name="java_home")
def fixture_java_home(tmp_path):
    """Directory of an installed java"""
    return Path(tmp_path)


@pytest.fixture(name="installed_java")
def fixture_installed_java(monkeypatch):
    """Let ``java --version`` report 25.0.5+8"""
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *_, **__: subprocess.CompletedProcess([], 0, JAVA_VERSION_OUTPUT),
    )


@pytest.fixture(name="head")
def fixture_head(monkeypatch):
    """Let ``requests.head`` redirect to a newer release than the installed"""
    head = Mock(
        return_value=Mock(headers={"Location": LOCATION.format("25.0.5.1%2B2")})
    )
    monkeypatch.setattr(requests, "head", head)
    return head


@pytest.mark.usefixtures("installed_java")
@pytest.mark.parametrize(
    "tag, expected",
    (
        ("25.0.5.1%2B2", True),
        ("25.0.5%2B8", False),
    ),
)
def test_needs_update(head, java_home, tag, expected):
    """The version of the redirect target is compared to the installed one"""
    head.return_value.headers["Location"] = LOCATION.format(tag)
    assert java._needs_update(java_home, URL) is expected


def test_needs_update_without_working_java(monkeypatch, java_home):
    """A java that cannot report its version is replaced"""

    def broken(*_, **__):
        raise OSError("no java")

    monkeypatch.setattr(subprocess, "run", broken)
    assert java._needs_update(java_home, URL) is True


@pytest.mark.usefixtures("installed_java")
@pytest.mark.parametrize(
    "failing_call",
    (
        # unreachable server
        lambda head: head,
        # error status
        lambda head: head.return_value.raise_for_status,
    ),
    ids=("offline", "error status"),
)
def test_needs_update_keeps_installation_on_failure(
    monkeypatch, head, java_home, failing_call
):
    """A failing lookup neither triggers an update nor blocks the next check"""
    failing_call(head).side_effect = requests.RequestException("failed")
    monkeypatch.setattr(java, "warn", lambda _: None)
    assert java._needs_update(java_home, URL) is False
    assert not Memoizer(java_home / "update_check.memo").items()


@pytest.mark.usefixtures("installed_java")
def test_needs_update_requests_once_per_day(head, java_home):
    """A second check within a day does not ask the server again"""
    assert java._needs_update(java_home, URL) is True
    assert java._needs_update(java_home, URL) is False
    assert head.call_count == 1


@pytest.mark.usefixtures("installed_java")
def test_needs_update_requests_again_after_a_day(head, java_home):
    """A check older than a day asks the server again"""
    with memoizer(java_home / "update_check.memo") as memo:
        memo.add(time.time() - 2 * java.ONE_DAY)

    assert java._needs_update(java_home, URL) is True
    assert head.call_count == 1
