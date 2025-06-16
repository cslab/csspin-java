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

.. _csspin_java.mvn:

===============
csspin_java.mvn
===============

The ``csspin_java.mvn`` plugin can be used to provision a desired Maven version
into the defined ``mvn.install_dir`` and making it available for use within
the context of csspin. It also provides the ``mvn``-task to execute Maven
commands.

.. The plugin is part of the "build" workflow, see `spin_conpod.stdworkflows
.. <http://qs.pages.contact.de/spin/spin_conpod/plugins/stdworkflows.html>`_ for
.. more information.

How to setup the ``csspin_java.java`` plugin?
#############################################

For using the ``csspin_java.java`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``csspin_java.mvn``

    plugin_packages:
        - csspin-java
    plugins:
        - csspin_java.mvn
    java:
        version: "19"

The provisioning of the plugins, its dependencies, Java, and Maven can be done
via the well-known ``spin provision``-command.

How to use the ``csspin_java.mvn`` plugin?
##########################################

After provision, the plugin can be used to execute Maven commands as follows:

.. code-block:: bash
   :caption: Using the ``csspin_java.mvn`` plugin

   spin mvn --help

How to use a local Maven installation?
######################################

If a local Maven installation is available, the ``mvn.install_dir`` can be
configured to point to the installation directory. The plugin will then use the
local installation instead of provisioning a new one.

An alternative solution is to use the ``mvn.use`` parameter to pass the Maven
executable.

``csspin_java.mvn`` schema reference
####################################

.. include:: mvn_schemaref.rst
