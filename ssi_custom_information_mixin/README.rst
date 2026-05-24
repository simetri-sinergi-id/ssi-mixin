.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

========================
Custom Information Mixin
========================

Description
-----------

**Custom Information Mixin** is a core mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides an extensible framework for attaching arbitrary user-defined
fields to any Odoo model without altering the database schema.

Any model that inherits ``mixin.custom_info`` gains a configurable set of
per-record custom data values driven by the assigned template.

Key Features
------------

- **Schema-free custom fields:** Add arbitrary properties to any model without
  database migrations.
- **Rich data types:** Supports text, integer, decimal, boolean, date,
  datetime, selection, and multiple-selection fields.
- **Template-driven:** Use ``custom_info.template`` to define which properties
  apply to each model, with domain or Python-code conditions.
- **Categorized properties:** Group related properties via
  ``custom_info.category`` for cleaner form layouts.
- **Controlled vocabulary:** Manage option sets (``custom_info.option_set``)
  for selection-type properties.
- **Mixin design:** Inheritable abstract model — zero boilerplate in consuming
  modules.

Use Cases / Context
-------------------

- **Customer profiles:** Attach industry-specific fields to partners without
  customising the partner model.
- **Product metadata:** Store supplier codes, certifications, or regulatory
  data per product.
- **Transaction documents:** Add contract-specific or project-specific fields
  to orders or invoices.
- **HR records:** Capture employee competencies, certificates, or custom HR
  attributes.
- **Multi-tenant setups:** Different companies can define different templates
  for the same model.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Custom Information Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. Add ``ssi_custom_information_mixin`` to the ``depends`` list of your module.
2. Inherit ``mixin.custom_info`` in your model class::

       class MyModel(models.Model):
           _name = "my.model"
           _inherit = ["mixin.custom_info", ...]
           _custom_info_create_page = True

3. The *Custom Information* tab is inserted automatically on the form view.
4. Configure templates via *Custom Information → Templates* to define which
   properties apply to your model records.

FAQ
---

**Is this module standalone?**
  No — it is a mixin foundation. Install it, then inherit it in your custom
  module.

**Which Odoo version is required?**
  Odoo 15.0.

**Can multiple templates exist for the same model?**
  Yes — templates are evaluated by sequence; the first matching template is
  applied.

**How do I contribute?**
  Fork the repository, create a branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_.
In case of trouble, please check there if your issue has already been
reported. If you spotted it first, help us smash it by providing detailed
and welcomed feedback.

Credits
-------

Contributors
~~~~~~~~~~~~

- Andhitia Rama <andhitia.r@gmail.com>
- Nur Azmi <azmimr67@gmail.com>
- Miftahussalam <miftahussalam08@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
