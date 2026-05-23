.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Many2one Configurator Mixin
===========================

Description
-----------

**Many2one Configurator Mixin** is a core mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides an abstract model — ``mixin.many2one_configurator`` — that
implements a three-strategy runtime filter for Many2one fields.

The three strategies are:

* **manual** — the allowed records are selected explicitly by the user.
* **domain** — a domain string (evaluated with ``safe_eval``) determines
  which records are allowed.
* **code** — arbitrary Python code is evaluated in a local dictionary
  (``env``, ``document``) and must assign a recordset to ``result``.

Concrete configurator models inherit this mixin and expose the strategy
fields to end users, enabling dynamic Many2one filtering without
hard-coded domains.

Key Features
------------

* **Three-Strategy Filter:** Supports manual, domain, and code-based
  filtering strategies for maximum flexibility.
* **Safe Eval Integration:** Domain and code strategies use Odoo's
  ``safe_eval`` for secure expression evaluation.
* **Mixin Design:** Built to be inherited — no views or menus added.
* **Minimal Footprint:** Depends only on ``base``.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

This mixin is ideal for developers who need configurable Many2one field
filtering at runtime without modifying source code:

* **Approval Rules:** Restrict which approvers are available based on
  document state or user-defined criteria.
* **Product Filters:** Dynamically limit selectable products per
  configuration record.
* **Partner Restrictions:** Allow or disallow partners based on custom
  domain expressions.
* **Custom Modules:** Add runtime-configurable Many2one domain logic to
  any custom Odoo module.

Installation
------------

1. Clone branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Many2one Configurator Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_m2o_configurator_mixin`` in your Odoo
   addons path.
2. **Enable:** In Odoo Apps, search for ``ssi_m2o_configurator_mixin``
   and install.
3. **Inherit:** In your configurator model, add::

      _inherit = ["mixin.many2one_configurator"]

4. **Call filter method:** Use
   ``self._m2o_configurator_get_filter(object_name, method_selection,
   manual_recordset, domain, python_code)`` to retrieve the filtered
   recordset.

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a
  dependency of your custom module.
* **Odoo Version?** Odoo 15.0.
* **What strategies are available?** ``manual``, ``domain``, ``code``.
* **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If
you spotted it first, help us smash it by providing detailed and
welcomed feedback.

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
