.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=============
QR Code Mixin
=============

Description
-----------

**QR Code Mixin** is a core mixin module in the **simetri-sinergi-id/ssi-mixin**
technology suite for Odoo 15. It provides a reusable abstract model —
``mixin.qr_code`` — that adds a computed QR-code image field to any model.

Any model inheriting from ``mixin.qr_code`` automatically gains:

* ``qr_image`` (Binary) — a computed QR-code image in PNG format encoded as
  Base64.
* Content strategy per model, configured via the extended ``ir.model``:
  either use the standard web URL of the record, or supply custom Python code
  that builds the string to encode.
* Optional automatic injection of a QR-code page into the form view by setting
  ``_qr_code_create_page = True`` on the inheriting model.

The module depends on the ``qrcode`` Python library and on ``ssi_decorator``
for automatic view injection.

Key Features
------------

* **Computed QR Image:** Adds a ``qr_image`` Binary field computed on-the-fly
  without storing data in the database.
* **Flexible Content Strategy:** Each model can use the default web URL or
  define custom Python code to generate the QR content via ``ir.model``
  configuration.
* **Auto View Injection:** Optionally injects a QR Code page tab into form
  views using ``ssi_decorator``.
* **Mixin Design:** Built to be inherited by other modules — no standalone
  functionality.
* **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

* **Document Traceability:** Attach a scannable QR code to any transactional
  document (invoices, sales orders, HR contracts) linking directly to the
  Odoo record.
* **Asset Tagging:** Print QR labels for fixed assets that deep-link to the
  asset record in Odoo.
* **Custom QR Content:** Supply Python code via ``ir.model`` to embed custom
  data (e.g. serial numbers, barcodes) instead of the record URL.
* **Mobile Access:** Allow warehouse or field staff to scan a QR code and
  open the relevant Odoo record on a mobile browser.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``)
3. Install the ``qrcode`` Python package: ``pip install qrcode``
4. Update the module list (must be in developer mode)
5. Go to menu *Apps → Apps → Main Apps*
6. Search for *QR Code Mixin*
7. Install the module

Installation & Usage
--------------------

1. **Inherit the mixin** in your model::

       class MySaleOrder(models.Model):
           _name = "my.sale.order"
           _inherit = ["my.sale.order", "mixin.qr_code"]
           _description = "My Sale Order"
           _qr_code_create_page = True  # auto-inject QR Code tab in form view

2. **View the QR code** on any record form — a *QR Code* tab will be
   automatically injected if ``_qr_code_create_page = True``.

3. **Customise QR content** via *Settings → Technical → Models*: find the
   model, open the *QR Content* tab, disable *Use Standard Content*, and
   write Python code that assigns the desired string to ``result``.

FAQ
---

* **Is this module standalone?** No. It is a mixin foundation intended to be
  inherited by other modules.
* **What is the default QR content?** The full web URL of the record
  (``web.base.url + /web?#id=...``).
* **Odoo Version?** Odoo 15.0.
* **Contribute?** Fork, branch, and submit a pull request on
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
* Michael Viriyananda <viriyananda.michael@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
