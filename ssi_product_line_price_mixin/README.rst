.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================================
Product Line Mixin - With Price
================================

Description
-----------

**Product Line Mixin - With Price** is a mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It extends ``mixin.product_line`` with a complete set of pricing fields
for use in transaction line models.

Any model that inherits from ``mixin.product_line_price`` automatically gains:

- ``currency_id`` and ``pricelist_id``, with ``allowed_pricelist_ids``
  dynamically filtered by the selected currency.
- ``price_unit`` and computed ``price_subtotal`` (= price_unit × quantity).
- Standard-price comparison fields: ``standard_price_unit``,
  ``standard_price_subtotal``, ``standard_price_unit_diff``, and
  ``standard_price_subtotal_diff`` — all derived from the selected pricelist.

Key Features
------------

- **Abstract Mixin Design:** Inherit ``mixin.product_line_price`` in any
  transaction line model with no structural view changes required.
- **Currency-Filtered Pricelists:** ``allowed_pricelist_ids`` is computed
  on-the-fly, showing only pricelists matching the selected currency.
- **Auto Price from Pricelist:** ``onchange_price_unit`` automatically fills
  ``price_unit`` from the selected pricelist when product or quantity changes.
- **Standard Price Comparison:** Computed fields reveal the difference between
  the selling price and the pricelist standard price at unit and subtotal level.
- **Monetary Fields:** All price fields use ``fields.Monetary`` linked to
  ``currency_id`` for proper multi-currency display.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin for any transaction model that requires product lines with
pricing, pricelist integration, and cost comparison:

- **Sales Quotations / Orders:** Add pricing fields to custom sale order line models.
- **Purchase Orders:** Compare purchase price against a reference pricelist.
- **Warehouse Transfers:** Track unit prices for stock movement valuation.
- **Custom Invoices:** Reuse pricing logic across different invoice line types.
- **Any Line Model:** Any model that needs product + quantity + price fields
  with pricelist support.

Simply set ``_inherit = ["mixin.product_line_price"]`` on your line model
and configure the rest via views.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``).
3. Update the module list (must be in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Product Line Mixin - With Price*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_product_line_price_mixin`` to your module's ``depends`` list
   in ``__manifest__.py``.
2. Inherit the mixin in your line model::

    _inherit = ["mixin.product_line_price"]

3. Optionally inherit the provided tree/form views via XPath to include
   pricing fields in your module's views.
4. Override ``_default_currency_id`` if a currency other than the company
   currency is required.

FAQ
---

- **Standalone?** No — it is a mixin foundation. Install it as a dependency
  of your custom module.
- **Odoo Version?** Odoo 15.0.
- **Does it require a pricelist?** No. ``pricelist_id`` is optional. If not
  set, standard price comparison fields will be 0.
- **Can I override the default currency?** Yes — override
  ``_default_currency_id`` in your model to return the desired default currency.
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

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://github.com/simetri-sinergi-id

This module is maintained by PT. Simetri Sinergi Indonesia.
