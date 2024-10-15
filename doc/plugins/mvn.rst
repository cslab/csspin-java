.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

.. _spin_java.mvn:

=============
spin_java.mvn
=============

The ``spin_java.mvn`` plugin can be used to provision a desired Maven version
into the defined ``mvn.install_dir`` and making it available for use within
the context of cs.spin. It also provides the ``mvn``-task to execute Maven
commands.

The plugin is part of the "build" workflow, see `spin_conpod.stdworkflows
<http://qs.pages.contact.de/spin/spin_conpod/plugins/stdworkflows.html>`_ for
more information.

How to setup the ``spin_java.java`` plugin?
###########################################

For using the ``spin_java.java`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``spin_java.mvn``

    plugin_packages:
        - spin_java
    plugins:
        - spin_java.mvn
    java:
        version: "19"

The provisioning of the plugins, its dependencies, Java, and Maven can be done
via the well-known ``spin provision``-command.

How to use the ``spin_java.mvn`` plugin?
########################################

After provision, the plugin can be used to execute Maven commands as follows:

.. code-block:: bash
   :caption: Using the ``spin_java.mvn`` plugin

   spin mvn --help

How to use a local Maven installation?
######################################

If a local Maven installation is available, the ``mvn.mavendir`` can be
configured to point to the installation directory. The plugin will then use the
local installation instead of provisioning a new one.

``spin_java.mvn`` schema reference
###################################

.. include:: mvn_schemaref.rst
