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

.. _csspin_java.java:

================
csspin_java.java
================

The ``csspin_java.java`` plugin can be used to provision a desired Java version
into the defined ``java.install_dir`` and making it available for use within
the context of csspin.

The plugin does not provide any tasks or commands to be executed.

How to setup the ``csspin_java.java`` plugin?
#############################################

For using the ``csspin_java.java`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``csspin_java.java``

    plugin_packages:
        - csspin-java
    plugins:
        - csspin_java.java
    java:
        version: "19"

The provisioning of the plugin, its dependencies and Java can be done via the
well-known ``spin provision``-command.

How to use a local Java installation?
#####################################

To use a local Java installation, the ``java.use`` can be leveraged as
demonstrated below:

.. code-block:: yaml
    :caption: Using a local Java installation

    spin -p java.use=java provision

    spin -p java.use=java run --version

``csspin_java.java`` schema reference
#####################################

.. include:: java_schemaref.rst
