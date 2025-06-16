|Latest Version| |Python| |License|

`csspin-java` is maintained and published by `CONTACT Software GmbH`_ and
serves plugins for building and developing CONTACT Elements-based applications
using the `csspin`_ task runner.

The following plugins are available:

- `csspin_java.java`: A plugin for installing Java
- `csspin_java.mvn`: A plugin for installing Apache Maven

Prerequisites
-------------

`csspin` is available on PyPI and can be installed using pip, pipx or any other
Python package manager, e.g.:

.. code-block:: console

   python -m pip install csspin

Using csspin-java
-----------------

The `csspin-java` package and its plugins can be installed by defining those
within the `spinfile.yaml` configuration file of your project.

.. code-block:: yaml

    spin:
      project_name: my_project

    # To develop plugins comfortably, install the packages editable as
    # follows and add the relevant plugins to the list 'plugins' below
    plugin_packages:
      - csspin-java

    # The list of plugins to be used for this project.
    plugins:
      - csspin_java.java


.. NOTE:: Assuming that `my_project` is a component based on CONTACT Elements CE16+.

.. _`CONTACT Software GmbH`: https://contact-software.com
.. |Python| image:: https://img.shields.io/pypi/pyversions/csspin-java.svg?style=flat
    :target: https://pypi.python.org/pypi/csspin-java/
    :alt: Supported Python Versions
.. |Latest Version| image:: http://img.shields.io/pypi/v/csspin-java.svg?style=flat
    :target: https://pypi.python.org/pypi/csspin-java/
    :alt: Latest Package Version
.. |License| image:: http://img.shields.io/pypi/l/csspin-java.svg?style=flat
    :target: https://www.apache.org/licenses/LICENSE-2.0.txt
    :alt: License
.. _`csspin`: https://pypi.org/project/csspin
