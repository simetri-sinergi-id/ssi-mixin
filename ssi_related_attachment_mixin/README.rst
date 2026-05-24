========================
Related Attachment Mixin
========================

Description
-----------

Related Attachment Mixin is a core mixin module in the **simetri-sinergi-id/ssi-mixin**
technology suite for Odoo. It provides a structured required-attachment framework that
can be mixed into any Odoo model to enforce document attachment requirements, verification
workflows, and categorised attachment tracking.

Key Features
------------

- **Attachment Templates:** Define which attachments are required for a given model using
  ordered template detail lines, with support for optional Python conditions.
- **Attachment Categories:** Group attachment requirements into named categories for clear
  display organisation on the document form.
- **Verification Workflow:** Supports user-based, group-based, combined, or Python-code-based
  verification methods per attachment requirement.
- **Mixin Design:** Inherit ``mixin.related_attachment`` in any model to automatically
  inject the related attachment page into its form view.
- **Import Wizard:** Upload or select existing attachments via a dedicated wizard.
- **ir.model Extension:** Specify trigger fields on a model that cause re-evaluation of
  attachment requirements when their values change.
- **Status Tracking:** Automatically computes aggregated counts (all, verified, unverified)
  and an overall attachment status (Not Needed / In Progress / Done).

Use Cases / Context
-------------------

- **Procurement:** Enforce mandatory supporting documents (e.g. quotation, PO approval)
  for purchase orders.
- **HR Onboarding:** Require employees to attach identity and contract documents before
  onboarding is complete.
- **Finance:** Ensure all invoices have valid supporting evidence before approval.
- **Custom Workflows:** Add structured attachment requirements to any custom module by
  simply inheriting the mixin.

Installation
------------

1. Clone the branch **15.0** of the repository: https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Related Attachment Mixin*
6. Install the module

Installation & Usage
--------------------

1. Install the module as described above.
2. Go to *Related Attachment → Templates* and create a template for the target model.
3. Add detail lines to the template specifying the required categories and verifiers.
4. Inherit ``mixin.related_attachment`` in your custom model and set
   ``_related_attachment_create_page = True`` to inject the attachment page.
5. On the document form, use the *Related Attachment* page to manage and verify attachments.

FAQ
---

- **Is this a standalone module?** No, it is a mixin foundation intended to be inherited
  by other modules that need structured attachment requirements.
- **Which Odoo version?** Odoo 15.0.
- **How do I contribute?** Fork the repository, create a branch, and submit a pull request
  on `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues <https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_.
In case of trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
-------

**Contributors:**

- **Core Development:**

  - Andhitia Rama <andhitia.r@gmail.com>
  - Michael Viriyananda <viriyananda.michael@gmail.com>

- **Community:** Thanks to all community members who reported issues and provided feedback.
- **Special Thanks:** To the Odoo Community Association (OCA) for the development guidelines
  and best practices.

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by **PT. Simetri Sinergi Indonesia**.

