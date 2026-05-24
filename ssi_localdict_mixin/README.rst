.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
Localdict Mixin
================

Description
-----------

**Localdict Mixin** is a lightweight mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides an abstract model — ``mixin.localdict`` — that supplies a
standard ``_get_default_localdict`` method.

The method assembles a ready-to-use safe-eval context dictionary
containing: ``env``, ``document``, ``time``, ``datetime``, ``dateutil``,
``timezone``, ``float_compare``, ``b64encode``, and ``b64decode``.

Models that need to evaluate user-supplied Python code (e.g. domain
filters, computed-by-code fields, or formula configurations) inherit this
mixin to avoid duplicating the context-building boilerplate.

Key Features
------------

- **Standard Localdict:** Provides a consistent ``_get_default_localdict``
  method for all models that evaluate Python expressions.
- **Safe-Eval Ready:** The context dictionary is pre-populated with
  commonly needed helpers: time utilities, timezone support, float
  comparison, and base64 encoding/decoding.
- **Mixin Design:** Built to be inherited — no views or menus added.
- **Minimal Footprint:** Depends only on ``base``.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

This mixin is ideal for any module that needs to evaluate dynamic
Python expressions configured by end users or administrators:

- **Formula Fields:** Models with code-based computed fields that need
  access to ORM helpers.
- **Domain Filters:** Dynamic domain expressions that reference ``env``
  or ``document``.
- **Configurable Business Logic:** Python-code fields in configuration
  records (e.g. payroll rules, approval conditions).
- **Custom Modules:** Any custom Odoo module that uses ``safe_eval`` with
  a standard context.

Simply set ``_inherit = ["mixin.localdict"]`` on your model and call
``self._get_default_localdict()`` to obtain the evaluation context.

Installation
------------

1. Clone branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Localdict Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_localdict_mixin`` in your Odoo addons
   path.
2. **Enable:** In Odoo Apps, search for ``ssi_localdict_mixin`` and
   install.
3. **Extend:** In your custom model, add ``"mixin.localdict"`` to
   ``_inherit``.
4. **Use:** Call ``self._get_default_localdict()`` to retrieve the
   standard safe-eval context dictionary.

FAQ
---

- **Standalone?** No — it is a mixin foundation. Install it as a
  dependency of your custom module.
- **Odoo Version?** Odoo 15.0.
- **What is in the localdict?** ``env``, ``document``, ``time``,
  ``datetime``, ``dateutil``, ``timezone``, ``float_compare``,
  ``b64encode``, ``b64decode``.
- **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If
you spotted it first, help us smash it by providing detailed and welcomed
feedback.

Credits
-------

Contributors
~~~~~~~~~~~~

* Andhitia Rama <andhitia.r@gmail.com>
* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
