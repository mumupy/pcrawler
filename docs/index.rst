.. pcrawler documentation master file, created by
   sphinx-quickstart on Tue Sep 25 09:21:33 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pcrawler's documentation!
====================================
pcrawler是一款python版本的爬虫程序，通过该爬虫程序可以非常快速方便的编写一个自己的爬虫程序。pcrawler主要
包含downloader、schedular、processor、storage四大组件组成。而且可以非常方便快捷的拓展各个组件。

The code is open source, and `available on GitHub`_.

.. _Read the docs: http://readthedocs.org/
.. _Sphinx: http://sphinx.pocoo.org/
.. _reStructuredText: http://sphinx.pocoo.org/rest.html
.. _CommonMark: http://commonmark.org/
.. _Subversion: http://subversion.tigris.org/
.. _Bazaar: http://bazaar.canonical.com/
.. _Git: http://git-scm.com/
.. _Mercurial: https://www.mercurial-scm.org/
.. _available on GitHub: https://github.com/mumupy/pcrawler.git

The main documentation for the site is organized into a couple sections:

* :ref:`user-docs`
* :ref:`about-docs`
* :ref:`feature-docs`

Information about development is also available:

* :ref:`dev-docs`
* :ref:`design-docs`

.. _user-docs:

.. toctree::
   :maxdepth: 2
   :caption: User Documentation

   get_start
   install

.. _about-docs:

.. toctree::
   :maxdepth: 2
   :caption: About Read the Docs

   README
   bloomFilter

.. _feature-docs:

.. toctree::
   :maxdepth: 2
   :glob:
   :caption: Feature Documentation

   README
   bloomFilter


.. _dev-docs:

.. toctree::
   :maxdepth: 2
   :caption: Developer Documentation

   README
   bloomFilter

.. _design-docs:

.. toctree::
   :maxdepth: 2
   :caption: Designer Documentation

   Theme <https://sphinx-rtd-theme.readthedocs.io/en/latest/>