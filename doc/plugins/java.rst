.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

.. _spin_java.java:

==============
spin_java.java
==============

The ``spin_java.java`` plugin can be used to provision a desired Java version
into the defined ``java.install_dir`` and making it available for use within
the context of cs.spin.

The plugin does not provide any tasks or commands to be executed.

How to setup the ``spin_java.java`` plugin?
###########################################

For using the ``spin_java.java`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``spin_java.java``

    plugin_packages:
        - spin_java
    plugins:
        - spin_java.java
    java:
        version: "19"

The provisioning of the plugin, its dependencies and Java can be done via the
well-known ``spin provision``-command.

How to use a local Java installation?
######################################

If a local Java installation is available, the ``java.install_dir`` can be
configured to point to the installation directory. The plugin will then use the
local installation instead of provisioning a new one.

``spin_java.java`` schema reference
###################################

.. include:: java_schemaref.rst
