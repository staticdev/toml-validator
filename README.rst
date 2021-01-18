TOML Validator
==============

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/toml-validator.svg
   :target: https://pypi.org/project/toml-validator/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/toml-validator
   :target: https://pypi.org/project/toml-validator
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/toml-validator
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/toml-validator/latest.svg?label=Read%20the%20Docs
   :target: https://toml-validator.readthedocs.io/
   :alt: Read the documentation at https://toml-validator.readthedocs.io/
.. |Tests| image:: https://github.com/staticdev/toml-validator/workflows/Tests/badge.svg
   :target: https://github.com/staticdev/toml-validator/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/staticdev/toml-validator/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/staticdev/toml-validator
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

CLI for tomlkit_.


Requirements
------------

You need Python 3.7.0 or above (latest 3.9 recommended) installed on your machine.


Installation
------------

You can install *TOML Validator* via pip_ from PyPI_:

.. code:: console

   $ pip install toml-validator


Usage
-----

.. code:: console

   $ toml-validator FILAPATH1 FILEPATH2 ...


It gives a green message for correct files and red message with errors.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*TOML Validator* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.


.. _tomlkit: https://pypi.org/project/tomlkit
.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/staticdev/toml-validator/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
