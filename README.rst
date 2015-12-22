=============================
django-app-gen
=============================

.. image:: https://badge.fury.io/py/django-app-gen.png
    :target: https://badge.fury.io/py/django-app-gen

.. image:: https://travis-ci.org/grantmcconnaughey/django-app-gen.png?branch=master
    :target: https://travis-ci.org/grantmcconnaughey/django-app-gen

Generate CRUD views, templates, URLs, and tests for a model.

Usage
-----

Generate views (with tests)...::

    python manage.py generate-views {model_name}

templates...::

    python manage.py generate-templates {model_name}

or everything.::

    python manage.py generate-all {model_name}


Documentation
-------------

The full documentation is at https://django-app-gen.readthedocs.org.

Quickstart
----------

Install django-app-gen::

    pip install django-app-gen

Then use it in a project::

    import appgen

Features
--------

* TODO

Running Tests
--------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements-text.txt
    (myenv) $ python runtests.py

Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/pydanny/cookiecutter-djangopackage