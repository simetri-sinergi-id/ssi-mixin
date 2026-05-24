.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================
res.partner Many2one Configurator Mixin
=========================================

Description
-----------

**res.partner Many2one Configurator Mixin** is a core mixin module in the
**@simetri-sinergi-id/ssi-mixin** technology suite for Odoo. It provides an
abstract model — ``mixin.res_partner_m2o_configurator`` — that adds
configurable filtering for ``res.partner`` Many2one fields using a
three-strategy pattern: manual selection, domain expression, or Python code.

Key Features
------------

- **Three Filter Strategies:** Choose between manual partner selection, domain
  expressions, or Python code to determine the available partner list.
- **Mixin Design:** Built to be inherited by other modules — no standalone
  functionality required.
- **Form View Injection:** Optionally injects the configuration widget into any
  inheriting module's form view via ``ssi_decorator``.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

This mixin is ideal for developers who need a consistent, configurable
``res.partner`` selector in their Odoo modules. Common use cases include:

- **Sales Configurator:** Restrict selectable customers per configuration.
- **HR Modules:** Limit partner selection to specific vendors or contacts.
- **Custom Workflows:** Filter partners dynamically based on domain or Python
  logic.
- **Reusable Components:** Add a standardized partner filter to any custom
  Odoo module without duplicating logic.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *res.partner Many2one Configurator Mixin*
6. Install the module

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_res_partner_m2o_configurator_mixin`` in your
   Odoo addons path.
2. **Enable:** In Odoo Apps, search for
   ``ssi_res_partner_m2o_configurator_mixin`` and install.
3. **Inherit:** In your model, inherit from
   ``mixin.res_partner_m2o_configurator`` to gain the three-strategy partner
   filter fields.
4. **Configure Form View:** Set
   ``_res_partner_m2o_configurator_insert_form_element_ok = True`` and
   ``_res_partner_m2o_configurator_form_xpath`` to auto-inject the
   configuration group into your form view.

FAQ
---

- **Standalone?** No, this is a mixin module — it must be inherited by another
  model to provide functionality.
- **Odoo Version?** Odoo 15.0.
- **Contribute?** Fork, branch, and submit a pull request on
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

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by **PT. Simetri Sinergi Indonesia**.

This module is maintained by the PT. Simetri Sinergi Indonesia.
