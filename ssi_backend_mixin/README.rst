.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=============
Backend Mixin
=============

Description
-----------

Backend Mixin is a core mixin module in the **simetri-sinergi-id/ssi-mixin**
technology suite for Odoo 15. It provides a reusable abstract base —
``backend_mixin`` — for *backend configuration* records that are scoped to a
company and can be toggled between ``draft`` and ``running`` states (e.g.
accounting settings, payroll parameters, HR configurations).

Key Features
------------

- **Company-Scoped Configuration:** Mandatory ``company_id`` field ensures
  each backend record belongs to exactly one company.
- **State Management:** ``draft`` / ``running`` state with ``action_running``
  and ``action_restart`` lifecycle actions.
- **Single Active Backend:** ``action_running`` automatically deactivates any
  other running record of the same type for the same company.
- **Company Pointer Integration:** Writes the active backend ID back to a
  configurable field on ``res.company`` via ``_backend_company_field``.
- **Master Data Foundation:** Inherits ``mixin.master_data`` for standardized
  ``name``, ``code``, ``active``, ``note``, chatter, and print-document
  support.

Use Cases / Context
-------------------

- **Accounting Backend:** Centralise accounting configuration per company with
  a single "running" record at any time.
- **Payroll Backend:** Store payroll parameters and activate them company-wide.
- **HR Backend:** Manage HR configuration objects that must be uniquely active
  per company.
- **Custom Backends:** Any module requiring a singleton-like, company-scoped
  configuration object can inherit this mixin.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Backend Mixin*
6. Install the module

Installation & Usage
--------------------

1. **Add to addons path:** Place ``ssi_backend_mixin`` in your Odoo addons
   path and install via the Apps menu.
2. **Inherit in your module:**

   .. code-block:: python

       class MyBackend(models.Model):
           _name = "my.backend"
           _inherit = ["backend_mixin"]
           _description = "My Backend"
           _backend_company_field = "my_backend_id"

3. **Add the company field:** Declare ``my_backend_id`` as a ``Many2one`` to
   ``my.backend`` on ``res.company``.
4. **Use the buttons:** The form view automatically includes *Running* and
   *Restart* buttons inherited from the mixin view.

FAQ
---

- **Can multiple records be running at the same time?** No. ``action_running``
  deactivates all other running records for the same company before activating
  the selected one.
- **What is ``_backend_company_field``?** The name of the field on
  ``res.company`` that stores the currently active backend record ID.
- **Is this module standalone?** No, it is a mixin foundation intended to be
  inherited by other modules.
- **Which Odoo version?** Odoo 15.0.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us improve by providing detailed and welcomed feedback.

Credits
-------

**Contributors:**

- Andhitia Rama <andhitia.r@gmail.com>
- Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by **PT. Simetri Sinergi Indonesia**.
