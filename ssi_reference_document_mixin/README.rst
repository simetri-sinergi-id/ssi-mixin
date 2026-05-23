========================
Reference Document Mixin
========================

Description
-----------

**Reference Document Mixin** is a mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo 15.
It provides a framework for attaching reference documents
(e.g. regulatory standards, guidelines, URLs) to any Odoo transactional document.

Key components:

* **reference_document_category** — master-data category for organising
  reference documents.
* **reference_document** — individual reference document with a URL, linked
  to a category and ordered by sequence.
* **reference_document_set** — named collection of reference documents;
  sets are attached to any document model.
* **mixin.reference_document** — abstract mixin that adds
  ``reference_document_set_ids`` and a computed flattened
  ``reference_document_ids``, with an optional auto-injected form-view page.

Key Features
------------

* **Abstract Mixin Design:** Inherit ``mixin.reference_document`` in any model
  to link reference document sets with minimal configuration.
* **Flattened Document List:** Automatically computes a deduplicated flat list
  of all reference documents across all attached sets.
* **Categorised & Ordered:** Documents are organised by category and sequence
  for a clean UI display.
* **Auto-injected Form Page:** Optionally inject a *Reference Documents* page
  into any form view by setting ``_reference_document_create_page = True``.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

* **Regulatory Compliance:** Attach relevant standards or regulations to
  work orders, contracts, or HR records.
* **Project Documentation:** Link SOPs, guidelines, and reference URLs to
  project tasks or deliverables.
* **Product References:** Associate technical datasheets or specification
  URLs with products or product categories.
* **Custom Modules:** Easily add reference document support to any custom
  Odoo module by inheriting the mixin.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Reference Document Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Install the module** following the steps above.
2. **Inherit the mixin** in your custom model::

       _inherit = ["mixin.reference_document"]

3. **Enable form-view page** (optional) — set on your model::

       _reference_document_create_page = True

4. **Configure sets** — go to *Reference Document → Sets*, create a set, and
   add reference documents to it.
5. **Assign sets** to your document records via the ``reference_document_set_ids``
   field, and the ``reference_document_ids`` computed field will automatically
   display all linked documents.

FAQ
---

* **Standalone?** No — it is a mixin foundation. Install it as a dependency
  of your custom module.
* **Odoo Version?** Odoo 15.0.
* **Can I add custom fields to a reference document?** Yes — inherit
  ``reference_document`` and extend it in your own module.
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
