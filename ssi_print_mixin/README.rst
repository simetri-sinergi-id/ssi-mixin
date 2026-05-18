.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==================
Print Policy Mixin
==================

Description
-----------

**Print Policy Mixin** is a core mixin module in the **@simetri-sinergi-id/ssi-mixin**
technology suite for Odoo 15. It provides a standardised, configurable
print-document framework that adds a *Print* button to any Odoo model via an
abstract mixin — without requiring changes to the base model's views.

The module ships three main components:

* **mixin.print_document** — abstract mixin that automatically injects a
  *Print* button into the form-view header and list-view header when
  ``_automatically_insert_print_button = True`` is set on the subclass.
* **print_document_type** — a named document type (scoped to a specific model)
  that groups the reports available for printing; its ``code`` is generated
  from a sequence.
* **ir.actions.report extension** — adds ``print_document_type_ids`` to link
  reports to types, a ``print_python_code`` condition evaluated at print time,
  and a ``print_multi`` flag for batch printing.

Key Features
------------

* **Auto-Injected Print Button:** One flag enables the Print button on both
  form and list views with zero view changes.
* **Document Type Grouping:** Group multiple reports per model under named
  types for a clean UI.
* **Python-Based Print Policy:** Control report visibility per record with a
  Python expression evaluated at runtime.
* **Batch / Multi-Record Printing:** Flag reports for batch printing from the
  list view.
* **Group-Based Access:** Optionally restrict individual reports to specific
  user groups.
* **Mixin Design:** Inherit ``mixin.print_document`` in any model — no
  structural changes required.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin whenever you need a flexible, policy-driven print button on a
custom Odoo model:

* **Sales Quotations:** Offer different quote layouts depending on the customer
  type via Python conditions.
* **HR Contracts:** Print contract PDFs with different templates per contract
  type.
* **Invoices / Delivery Orders:** Group invoice and packing-slip reports under
  separate document types.
* **Batch Operations:** Allow warehouse staff to print multiple delivery slips
  in one click from the list view.
* **Custom Transactional Models:** Any model that needs contextual, role-based
  report selection.

Simply inherit ``mixin.print_document``, set
``_automatically_insert_print_button = True``, and configure **Print Document
Types** via the menu.

Installation
------------

To install this module, you need to:

1. Clone branch **15.0** of the repository
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``)
3. Update the module list (Must be on developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Print Policy Mixin*
6. Install the module

Installation & Usage
--------------------

After installation:

1. Go to *Reporting → Print Document Types* to create types and link reports.
2. In your custom model, inherit the mixin::

    class MyModel(models.Model):
        _name = "my.model"
        _inherit = ["mixin.print_document", "my.model"]
        _automatically_insert_print_button = True

3. The *Print* button will appear automatically in the form header and list
   header. Users select a document type and report via the wizard.

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a dependency
  of your custom module.
* **Odoo Version?** Odoo 15.0.
* **Can I control which users see which reports?** Yes — use
  ``print_python_code`` on the report or restrict via Odoo groups.
* **Batch printing from list view?** Yes — enable ``print_multi`` on the
  report action.
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

* Andhitia Rama <andhitia.r@gmail.com>
* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
