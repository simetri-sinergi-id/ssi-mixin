.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Company Currency Mixin
======================

Description
-----------

**Company Currency Mixin** is a lightweight mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides a reusable abstract model -- ``mixin.company_currency`` -- that
adds a company field and its derived currency field to any model.

Any model that inherits from ``mixin.company_currency`` automatically gains:

- A mandatory ``company_id`` (``res.company``) field defaulting to the
  current user's company.
- A stored, related ``company_currency_id`` field that always reflects the
  selected company's currency.

Monetary fields on inheriting models can set
``currency_field='company_currency_id'`` to format amounts in the company's
currency without any extra boilerplate.

Key Features
------------

- **Abstract Mixin Design:** Inherit ``mixin.company_currency`` in any model
  -- no structural view changes required.
- **Auto Company Default:** ``company_id`` defaults to the current user's
  company automatically.
- **Derived Currency:** ``company_currency_id`` is always in sync with the
  selected company's currency via a stored related field.
- **Monetary Field Ready:** Set ``currency_field='company_currency_id'`` on
  any monetary field to enable proper currency display.
- **Minimal Footprint:** Depends only on ``base`` -- no heavy extra
  dependencies.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin for any transactional or master-data model that needs
multi-company currency awareness:

- **Sale/Purchase Orders:** Ensure monetary fields are always displayed in
  the owning company's currency.
- **Invoices & Payments:** Standardise company currency derivation across
  accounting documents.
- **Warehouse Transfers:** Attach cost fields with correct currency to stock
  transfer lines.
- **Custom Transactions:** Any model with monetary amounts that must respect
  multi-company currency settings.

Simply set ``_inherit = ["mixin.company_currency"]`` on your model and
reference ``company_currency_id`` in your monetary fields.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``).
3. Update the module list (must be in developer mode).
4. Go to menu *Apps -> Apps -> Main Apps*.
5. Search for *Company Currency Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_company_currency_mixin`` to your module's ``depends`` list in
   ``__manifest__.py``.
2. Inherit the mixin in your model::

    _inherit = ["mixin.company_currency"]

3. On any monetary field, add ``currency_field="company_currency_id"``::

    amount = fields.Monetary(
        string="Amount",
        currency_field="company_currency_id",
    )

FAQ
---

- **Standalone?** No -- it is a mixin foundation. Install it as a dependency
  of your custom module.
- **Odoo Version?** Odoo 15.0.
- **Is company_id required?** Yes -- it defaults to the current user's company
  but can be changed.
- **Is company_currency_id stored?** Yes -- it is a stored related field so it
  can be used in domain filters and reports.
- **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

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
* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://github.com/simetri-sinergi-id

This module is maintained by PT. Simetri Sinergi Indonesia.
