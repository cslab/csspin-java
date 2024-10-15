.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

======================
Installation and setup
======================

cs.spin must be installed beforehand, this can be done as documented at
http://qs.pages.contact.de/spin/cs.spin/installation.html.

For leveraging plugins from within the ``spin_java`` plugin-package for
``cs.spin``, the plugin-package must be added to the list of plugin-packages
within a project's ``spinfile.yaml``.

.. code-block:: yaml
    :caption: Example: ``spinfile.yaml`` setup to enable the java and mvn plugin

    plugin_packages:
        - spin_java
    plugins:
        - spin_java:
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

    spin docs --help
