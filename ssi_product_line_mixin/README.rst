.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===================
Product Line Mixin
===================

Description
-----------

**Product Line Mixin** is a foundational mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides a reusable abstract model -- ``mixin.product_line`` -- for
product-line child records (detail rows) in transactional documents.

Any model that inherits from ``mixin.product_line`` automatically gains:

- ``product_id`` (``product.product``) and ``name`` (description),
  auto-filled via onchange from the selected product.
- ``uom_quantity``, ``uom_id`` (with ``allowed_uom_ids`` filtered by the
  product's UoM category), and a computed ``quantity`` converted to the
  product's base UoM.
- ``sequence`` field for ordering lines, auto-filled from the product's
  sequence.
- ``note`` -- free-text remark per line.
- Configurable name source via ``_field_for_name`` class attribute
  (default: ``display_name``).

Key Features
------------

- **Abstract Mixin Design:** Inherit ``mixin.product_line`` in any transaction
  line model -- no structural view changes required.
- **Auto-fill Description & UoM:** Onchange handlers automatically populate
  ``name`` and ``uom_id`` when a product is selected.
- **UoM Category Filter:** ``allowed_uom_ids`` limits UoM selection to the
  product's UoM category, preventing invalid conversions.
- **Base-UoM Quantity:** ``quantity`` is always computed in the product's base
  UoM for consistent downstream calculations.
- **Configurable Name Source:** Override ``_field_for_name`` to use any product
  field (e.g., ``name``, ``default_code``) as the line description.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin for any transaction document that requires product detail lines:

- **Sale Order Lines:** Standardise product + quantity + UoM on custom sale
  order line models.
- **Purchase Order Lines:** Reuse the same line structure on purchase or RFQ
  models.
- **Warehouse Transfer Lines:** Track product, quantity, and UoM for stock
  movements.
- **Work Order Lines:** Define material or service lines on manufacturing work
  orders.
- **Any Transaction Line:** Any child model that needs product + quantity + UoM
  fields.

Simply set ``_inherit = ["mixin.product_line"]`` on your line model and extend
further with price or account mixins as needed.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``).
3. Update the module list (must be in developer mode).
4. Go to menu *Apps -> Apps -> Main Apps*.
5. Search for *Product Line Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_product_line_mixin`` to your module's ``depends`` list in
   ``__manifest__.py``.
2. Inherit the mixin in your line model::

    _inherit = ["mixin.product_line"]

3. Optionally set ``_field_for_name = "default_code"`` (or any product field)
   to control the auto-filled description.
4. Inherit the provided tree/form views via XPath to include line fields in
   your module's views.

FAQ
---

- **Standalone?** No -- it is a mixin foundation. Install it as a dependency of
  your custom module.
- **Odoo Version?** Odoo 15.0.
- **Can I change which product field fills the description?** Yes -- set
  ``_field_for_name = "default_code"`` (or any product field) on your concrete
  model.
- **Does it handle UoM conversion?** Yes -- ``quantity`` is always converted to
  the product's base UoM using Odoo's built-in ``_compute_quantity``.
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
