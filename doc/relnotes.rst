.. -*- coding: utf-8 -*-
   Copyright (C) 2025 CONTACT Software GmbH
   https://www.contact-software.com/

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

.. This document contains the release notes for csspin-java. Each release is
   documented in a separate section, starting with the most recent release at
   the top.

   The release section must be renamed to the actual release tag with a prefixed
   "v". The date of the release must be in the format `Month Day, Year`/`"%B %d,
   %Y"`.

    At least one of these subsections must be present for each release:

    - Enhancements
    - Bug Fixes
    - Chores

    Each of these subsection must contain a bulleted list of changes made in the
    release. Each bullet must contain a short description of the change and a
    reference to the issue or merge request where the change was made.

    If required, the additional subsections can be added:

    - Breaking Changes
    - Migration Guide

    These additional subsections must contain a concise description of the
    changes required to migrate from the previous version to the new version.
    This may include code examples, configuration changes, or other relevant
    information to assist users in updating their implementations.

    Example:

    v2.0.2
    ======

    December 10, 2025

    Chores
    ------

    - Add release notes to the documentation structure (`#27 <https://code.contact.de/pod/components/csspin-java/-/issues/27>`_)

=============
Release Notes
=============

v3.1.0
======

November 19, 2026

Enhancements
------------

- Let the java plugin update the provisioned Java at most once per day and
  major version (`!52
  <https://code.contact.de/pod/components/csspin-java/-/merge_requests/52>`_)

v3.0.0
======

November 09, 2026

Breaking Changes
----------------

- Drop Python 3.9 support (`#31
  <https://code.contact.de/pod/components/csspin-java/-/issues/31>`_)

Bug Fixes
---------

- Fix ``mvn`` help texts and stop mutating ``mvn.opts`` (`#34
  <https://code.contact.de/pod/components/csspin-java/-/issues/34>`_)

Chores
------

- Add release notes to the documentation structure (`#27 <https://code.contact.de/pod/components/csspin-java/-/issues/27>`_)
- Warn when ``java.use`` and ``java.version`` are both set, same for ``mvn`` (`#25
  <https://code.contact.de/pod/components/csspin-java/-/issues/25>`_)
- Change the default Apache Maven install directory to
  ``{spin.data}/apache-maven/<version>`` (`#28
  <https://code.contact.de/pod/components/csspin-java/-/issues/28>`_)
- Add repository URL to the wheel metadata (`#29
  <https://code.contact.de/pod/components/csspin-java/-/issues/29>`_)
- Update release process documentation and contribution guideline (`#30
  <https://code.contact.de/pod/components/csspin-java/-/issues/30>`_)
- Document CONTACT Community as release notification channel (`#32
  <https://code.contact.de/pod/components/csspin-java/-/issues/32>`_)
- Add SonarQube analysis (`!44
  <https://code.contact.de/pod/components/csspin-java/-/merge_requests/44>`_)
- Update CI includes and stale references after move to ``pod/components`` (`!45
  <https://code.contact.de/pod/components/csspin-java/-/merge_requests/45>`_)
- Add CEDM component portfolio update to release procedure (`!46
  <https://code.contact.de/pod/components/csspin-java/-/merge_requests/46>`_)
- Fix toml formatting (`!47
  <https://code.contact.de/pod/components/csspin-java/-/merge_requests/47>`_)
- Run Linux CI on Python 3.11 instead of 3.10 (`#35
  <https://code.contact.de/pod/components/csspin-java/-/issues/35>`_)
