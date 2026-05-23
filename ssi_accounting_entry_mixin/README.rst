.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================
Accounting Entry Mixin
======================

Description
-----------

**Accounting Entry Mixin** is a core mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides a set of composable abstract models that standardise the
creation, posting, and deletion of accounting entries
(``account.move`` and ``account.move.line``) from transactional documents.

The module ships four composable mixins:

* **mixin.account_move** — high-level helper for the journal-entry *header*:
  creates, posts, and cancels an ``account.move`` record with configurable
  field-name pointers and optional tax computation support.
* **mixin.account_move_single_line** — creates one ``account.move.line``
  inside an existing move; the normal direction (debit vs. credit) and all
  source fields are driven by class-level attributes.
* **mixin.account_move_double_line** — creates a balanced debit/credit pair
  of move lines in one call; each side is independently configurable.
* **mixin.tax_line** — ready-to-use child-record model for tax lines that
  references the appropriate tax account.

Concrete ``_with_field`` variants of each mixin add the actual Odoo storage
fields (``move_id``, ``move_line_id``, ``realized``, etc.) for cases where the
inheriting model needs to persist the generated entry references.

Key Features
------------

* **Abstract Mixin Design:** Inherit any of the accounting mixins in your
  transactional model with zero structural view duplication.
* **Configurable Field Pointers:** All source field names are driven by
  class-level attributes so the mixin adapts to any model layout.
* **Single-Line Entry:** Post one journal item (debit or credit) via
  ``mixin.account_move_single_line``.
* **Double-Line Entry:** Post a balanced debit/credit pair via
  ``mixin.account_move_double_line``.
* **Tax Computation:** Built-in tax grouping and tax line creation via
  ``mixin.account_move`` and ``mixin.tax_line``.
* **Realized Flag:** Related boolean that turns ``True`` when the linked
  journal item is fully reconciled.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use these mixins whenever a transactional document needs to generate
accounting entries automatically:

* **Payment Documents:** Post a single move line when a payment is confirmed.
* **Accrual Documents:** Post debit/credit pairs for accrual and reversal.
* **Tax-Inclusive Transactions:** Compute and store tax lines alongside the
  main journal entry.
* **Custom Financial Documents:** Any document that creates ``account.move``
  records and needs to track reconciliation status.

Installation
------------

1. Clone branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Accounting Entry Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_accounting_entry_mixin`` to your module's ``depends`` list.
2. Inherit one or more mixins in your model::

    class MyDocument(models.Model):
        _name = "my.document"
        _inherit = [
            "mixin.transaction",
            "mixin.account_move",
            "mixin.account_move_double_line",
        ]

3. Override the class-level field-name attributes as needed::

    _journal_id_field_name = "journal_id"
    _move_id_field_name = "move_id"
    _debit_account_id_field_name = "debit_account_id"
    _credit_account_id_field_name = "credit_account_id"

4. Call ``_create_standard_move()`` and ``_create_standard_ml()`` from your
   business-logic methods to generate the accounting entry.

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a dependency
  of your custom transactional module.
* **Odoo Version?** Odoo 15.0.
* **Can I use only one line instead of two?** Yes — inherit
  ``mixin.account_move_single_line`` for a single journal item.
* **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed
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
