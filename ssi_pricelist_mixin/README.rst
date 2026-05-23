.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

================
Pricelist Mixin
================

Description
-----------

**Pricelist Mixin** is an abstract mixin module in the **simetri-sinergi-id/ssi-mixin**
technology suite for Odoo. It provides currency-aware pricelist selection that can be
mixed into any transactional model to ensure the selected pricelist always matches the
transaction currency.

Any model that inherits from ``mixin.pricelist`` automatically gains:

* ``currency_id`` (``res.currency``) — the transaction currency.
* ``pricelist_id`` (``product.pricelist``) — the selected pricelist.
* ``allowed_pricelist_ids`` — a computed Many2many that filters available
  pricelists to those matching the selected currency.
* ``onchange_pricelist_id`` — clears the pricelist whenever the currency
  changes to prevent currency/pricelist mismatches.

Key Features
------------

* **Currency-Aware Filtering:** Available pricelists are automatically filtered
  to match the selected currency, preventing invalid combinations.
* **Mixin Design:** Built to be inherited by any transactional model — sales
  orders, purchase orders, custom documents, etc.
* **Automatic Reset:** Pricelist is cleared on currency change via onchange,
  keeping data consistent at all times.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

This mixin is ideal for developers building transactional documents that require
a pricelist consistent with a specific currency:

* **Sales Documents:** Attach a pricelist to sales orders or quotations scoped
  to the document currency.
* **Purchase Documents:** Ensure supplier pricelists align with purchase currency.
* **Custom Transactions:** Add currency-constrained pricelist selection to any
  custom Odoo model with a single ``_inherit``.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Pricelist Mixin*
6. Install the module

Installation & Usage
--------------------

1. **Install:** Place ``ssi_pricelist_mixin`` in your Odoo addons path and
   install via the Apps menu.
2. **Inherit:** Add ``mixin.pricelist`` to your model's ``_inherit`` list::

       class MySalesDocument(models.Model):
           _name = "my.sales.document"
           _inherit = [
               "mixin.pricelist",
           ]

3. **View:** Add ``currency_id`` and ``pricelist_id`` to your form view. Use
   ``allowed_pricelist_ids`` as the domain source for ``pricelist_id`` to
   limit selectable pricelists.

FAQ
---

* **Standalone?** No, it is a mixin foundation intended to be inherited by
  other modules that require currency-consistent pricelist selection.
* **Odoo Version?** Odoo 15.0 or above.
* **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of trouble,
please check there if your issue has already been reported. If you spotted it
first, help us smash it by providing detailed and welcomed feedback.

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

