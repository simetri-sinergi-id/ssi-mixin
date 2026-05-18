.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============
Sequence Mixin
==============

Description
-----------

**Sequence Mixin** is a core mixin module in the **@simetri-sinergi-id/ssi-mixin**
technology suite for Odoo 15. It provides a configurable, reusable document-numbering
framework that can be mixed into any transactional model to automatically generate
document numbers (codes) based on flexible criteria and sequence templates.

The module ships two main components:

* **sequence.template** — a master-data record that maps a model and a set of
  applicability criteria (Python expression or domain filter) to an ``ir.sequence``
  with optional custom prefix/suffix computation.
* **mixin.sequence** — an abstract mixin that adds ``_create_sequence()`` to
  auto-select the applicable template and apply the generated number to the
  configured field.

Key Features
------------

* **Template-Based Numbering:** Define multiple sequence templates per model;
  the first matching template is used.
* **Flexible Applicability:** Determine which template applies via a Python
  expression or an Odoo domain filter.
* **Sequence Selection Methods:** Use a standard ``ir.sequence`` or a Python
  expression to pick the sequence.
* **Custom Prefix & Suffix:** Optionally compute and prepend/append dynamic
  strings (e.g. year, month) around the sequence number.
* **Date-Aware:** Passes the document date to ``ir.sequence`` so date-based
  reset periods work correctly.
* **Mixin Design:** Zero-intrusion — inherit ``mixin.sequence`` in any model
  to get the full capability.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin whenever you need automatic, rule-based document numbering in a
custom Odoo module:

* **Sales Orders / Invoices:** Generate numbers like ``SO/2025/001`` with
  date-based reset.
* **HR Documents:** Different numbering sequences per department or contract type.
* **Multi-Company:** Separate sequences per company entity.
* **Custom Transactional Models:** Any model requiring structured reference numbers.

Simply inherit ``mixin.sequence``, configure a **Sequence Template** via the menu,
and call ``_create_sequence()`` at the appropriate state transition.

Installation
------------

To install this module, you need to:

1. Clone branch **15.0** of the repository
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your configuration (``addons-path``)
3. Update the module list (Must be on developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Sequence Mixin*
6. Install the module

Installation & Usage
--------------------

After installation:

1. Go to *Sequence → Templates* to create sequence templates for your models.
2. In your custom model, inherit ``mixin.sequence``::

    class MyModel(models.Model):
        _name = "my.model"
        _inherit = ["mixin.sequence", "my.model"]

3. Call ``self._create_sequence()`` at the state transition where the document
   number should be generated (e.g. inside ``action_confirm``).

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a dependency of
  your custom module.
* **Odoo Version?** Odoo 15.0.
* **Can I have multiple templates for one model?** Yes. Templates are evaluated
  in ascending ``sequence`` order; the first matching one wins.
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
* Nur Azmi <azmimr67@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
