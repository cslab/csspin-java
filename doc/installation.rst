.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
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

======================
Installation and setup
======================

`csspin`_ must be installed beforehand, this can be done as documented at
http://qs.pages.contact.de/spin/csspin/installation.html.

For leveraging plugins from within the ``csspin_java`` plugin-package for
``csspin``, the plugin-package must be added to the list of plugin-packages
within a project's ``spinfile.yaml``.

.. code-block:: yaml
    :caption: Example: ``spinfile.yaml`` setup to enable the java and mvn plugin

    plugin_packages:
        - csspin_java
    plugins:
        - csspin_java:
            - java
            - mvn
    java:
        version: '19'

After the setup is done, the plugin-package can be provisioned by executing the
following command within the project's directory:

.. code-block:: console

    spin provision

The plugins defined in the plugins section of the ``spinfile.yaml`` can now be
used, using:

.. code-block:: console

    spin mvn --help
