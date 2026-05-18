.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=================
Master Data Mixin
=================

Description
-----------

**Master Data Mixin** is a foundational mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15. It provides
an abstract model — ``mixin.master_data`` — that serves as a reusable base
for **master/reference data** records.

Any model that inherits from ``mixin.master_data`` automatically gains:

* **Standard fields** — ``name`` (translatable), ``code`` (unique identifier),
  ``active`` (archive / restore), and ``note`` (free-text remarks).
* **Sequence generation** — a *Generate Code* button that assigns a
  sequence-based code from a configured sequence template.  Records whose
  ``code`` is ``'/'`` are treated as “unassigned” and can receive an automatic
  code at any time.
* **Unique-code constraint** — prevents two records of the same model from
  sharing the same non-slash code.
* **Chatter integration** — inherits ``mail.thread`` and
  ``mail.activity.mixin``, giving the form view a full messaging thread and
  activity scheduler.
* **Print-document support** — inherits ``mixin.print_document`` and
  automatically injects a *Print* button into the form header.
* **Configurable display name** — set ``_show_code_on_display_name = True``
  on a concrete model to render the display name as ``[code] name`` throughout
  the UI.

Key Features
------------

* **Abstract Mixin Design:** Inherit ``mixin.master_data`` in any model — no
  structural view changes required.
* **Auto Sequence Code:** Click *Generate Code* to assign a unique,
  sequence-based code from a configured template.
* **Duplicate Code Guard:** Built-in constraint prevents duplicate codes across
  records of the same model.
* **Archive / Restore:** The ``active`` flag allows archiving obsolete master
  data without deleting it.
* **Chatter & Activities:** Full messaging thread and activity scheduling on
  every inheriting model.
* **Integrated Print Button:** Auto-injected Print button via
  ``mixin.print_document``.
* **Display Name Toggle:** Optionally show ``[code] name`` format via a single
  class attribute.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin for any static reference table that modules configure once and
reuse across transactions:

* **Product Types / Categories:** Define categories with codes and reuse
  across sale/purchase orders.
* **Work-Order Categories:** Standardise work-order types with unique codes
  for reporting.
* **School Grades / Levels:** Manage academic grade structures as archivable
  master data.
* **Payment Terms:** Custom payment term types with sequence-generated codes.
* **Any Reference Table:** Any lookup/configuration table that benefits from
  codes, archiving, and chatter.

Simply set ``_inherit = ["mixin.master_data"]`` on your model and configure
the rest via the UI.

Installation
------------

To install this module, you need to:

1. Clone branch **15.0** of the repository
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``)
3. Update the module list (Must be on developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Master Data Mixin*
6. Install the module

Installation & Usage
--------------------

After installation:

1. In your custom model, inherit the mixin::

    class MyMasterData(models.Model):
        _name = "my.master_data"
        _inherit = ["mixin.master_data"]
        _description = "My Master Data"

2. Optionally configure display name format::

    _show_code_on_display_name = True

3. Go to the model’s list view and use the *Generate Code* header button to
   assign sequence-based codes to records whose current code is ``'/'``.

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a dependency
  of your custom module.
* **Odoo Version?** Odoo 15.0.
* **What if I don’t need sequence codes?** Leave ``code`` as ``'/'``. The
  constraint ignores slash codes.
* **Can I hide the code field from the view?** Yes — override the inherited
  view via XPath in your custom module.
* **Contribute?** Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of trouble,
please check there if your issue has already been reported. If you spotted it
first, help us smash it by providing detailed and welcomed feedback.

Credits
=======

Contributors
------------

* Michael Viriyananda <viriyananda.michael@gmail.com>
* Andhitia Rama <andhitia.r@gmail.com>
* Asrul Bastian Yunas <asrulbastianyunas@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
