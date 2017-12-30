pdutil
######
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

Utilities for pandas.

.. code-block:: python

  import pdutil
  for subdf in pdutil.iter.sub_dfs_by_size(df, 2):
    print(subdf)

.. contents::

.. section-numbering::


Installation
============

.. code-block:: bash

  pip install pdutil


Basic Use
=========

``pdutil`` is divided into several sub-modules by functionality:

display
-------

Functions related to displaying ``pandas`` DataFrames:

  * ``df_string`` - Returns a nicely formatted string for the given dataframe.
  * ``pandas_big_frame_setup`` - Sets pandas to display really big data frames.
  * ``df_to_html`` - Return a nicely formatted HTML code string for the given dataframe.

iter
----

Functions related to iterating over ``pandas`` dataframes:

  * ``sub_dfs_by_size`` - Get a generator yielding consecutive sub-dataframes of the given size.
  * ``sub_dfs_by_num`` - Get a generator yielding num consecutive sub-dataframes of the given df. 

Contributing
============

Package author and current maintainer is Shay Palachy (shay.palachy@gmail.com); You are more than welcome to approach him for help. Contributions are very welcomed.

Installing for development
----------------------------

Clone:

.. code-block:: bash

  git clone git@github.com:shaypal5/pdutil.git


Install in development mode:

.. code-block:: bash

  cd pdutil
  pip install -e .


Running the tests
-----------------

To run the tests use:

.. code-block:: bash

  pip install pytest pytest-cov coverage
  cd pdutil
  pytest


Adding documentation
--------------------

The project is documented using the `numpy docstring conventions`_, which were chosen as they are perhaps the most widely-spread conventions that are both supported by common tools such as Sphinx and result in human-readable docstrings. When documenting code you add to this project, follow `these conventions`_.

.. _`numpy docstring conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt
.. _`these conventions`: https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt


Credits
=======

Created by Shay Palachy (shay.palachy@gmail.com).


.. |PyPI-Status| image:: https://img.shields.io/pypi/v/shleem.svg
  :target: https://pypi.python.org/pypi/shleem

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/shleem.svg
   :target: https://pypi.python.org/pypi/shleem

.. |Build-Status| image:: https://travis-ci.org/shaypal5/shleem.svg?branch=master
  :target: https://travis-ci.org/shaypal5/shleem

.. |LICENCE| image:: https://img.shields.io/pypi/l/shleem.svg
  :target: https://pypi.python.org/pypi/shleem

.. |Codecov| image:: https://codecov.io/github/shaypal5/shleem/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/shleem?branch=master
