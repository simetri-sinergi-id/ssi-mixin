.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================================
res.currency Many2one Configurator Mixin
========================================

Description
-----------

**res.currency Many2one Configurator Mixin** is a mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.

It provides an abstract model — ``mixin.res_currency_m2o_configurator`` — that
adds configurable filtering for ``res.currency`` Many2one fields using the
three-strategy pattern from ``ssi_m2o_configurator_mixin`` (manual, domain, or
Python code).

Key Features
------------

- **Three-Strategy Filter:** Supports manual, domain, and Python-code-based
  filtering strategies for ``res.currency`` Many2one fields.
- **Mixin Design:** Built to be inherited by type/category models — no views or
  menus added.
- **Form Element Injection:** Optionally injects the configuration widget into
  the host model's form view via ``ssi_decorator``.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

This mixin is used by type/category models that need to restrict which
currencies a derived transactional record may choose. Common use cases:

- **Payment Type Configuration:** Restrict allowed currencies per payment type.
- **Invoice Template:** Limit currency choices per invoice template category.
- **Custom Configurators:** Any model that must expose a configurable currency
  filter to end users.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``).
3. Update the module list (must be on developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *res.currency Many2one Configurator Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_res_currency_m2o_configurator_mixin`` to the ``depends`` list of
   your custom module.
2. Inherit the mixin in your type/category model::

       class MyTypeModel(models.Model):
           _name = "my.type.model"
           _inherit = ["mixin.res_currency_m2o_configurator"]
           _res_currency_m2o_configurator_insert_form_element_ok = True
           _res_currency_m2o_configurator_form_xpath = "//field[@name='name']"

3. Use the ``currency_selection_method``, ``currency_ids``,
   ``currency_domain``, and ``currency_python_code`` fields on your model to
   configure the allowed currencies.

FAQ
---

**Is this a standalone module?**
  No — it is a mixin foundation. Install it as a dependency of your custom
  module.

**Which Odoo version is supported?**
  Odoo 15.0.

**What strategies are available?**
  ``manual``, ``domain``, and ``code``.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
-------

Contributors
~~~~~~~~~~~~

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
