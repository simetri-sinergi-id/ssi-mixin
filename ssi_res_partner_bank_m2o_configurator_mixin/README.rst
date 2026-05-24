.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

============================================
res.partner.bank Many2one Configurator Mixin
============================================

Description
-----------

``ssi_res_partner_bank_m2o_configurator_mixin`` provides an abstract Odoo
model — ``mixin.res_partner_bank_m2o_configurator`` — that adds
configurable filtering for ``res.partner.bank`` (bank account) Many2one
fields using a three-strategy pattern: manual selection, domain filter,
or Python code evaluation.

Key Features
------------

- **Three Filter Strategies:** Choose between manual selection, domain
  expression, or Python code to determine available bank accounts.
- **Mixin Design:** Inherit this mixin in any module that needs a
  configurable ``res.partner.bank`` Many2one field.
- **Form View Integration:** Optionally inject the configuration widget
  into an existing form view via the decorator pattern.
- **Deep Integration:** Works seamlessly with ``ssi_decorator`` and
  ``ssi_m2o_configurator_mixin`` patterns.

Use Cases / Context
-------------------

- **Payment Documents:** Restrict selectable bank accounts on payment
  forms based on partner or company rules.
- **Vendor Bills / Expenses:** Dynamically filter bank accounts depending
  on the vendor or business unit.
- **Custom Workflows:** Any document model that requires a filtered
  partner bank Many2one field.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *res.partner.bank Many2one Configurator Mixin*
6. Install the module

Installation & Usage
--------------------

1. Add ``ssi_res_partner_bank_m2o_configurator_mixin`` to your module's
   ``depends`` list.
2. Inherit ``mixin.res_partner_bank_m2o_configurator`` in your model:

   .. code-block:: python

       class MyModel(models.Model):
           _name = "my.model"
           _inherit = [
               "mixin.res_partner_bank_m2o_configurator",
           ]
           _res_partner_bank_m2o_configurator_insert_form_element_ok = True
           _res_partner_bank_m2o_configurator_form_xpath = "//field[@name='partner_id']"

3. The mixin will inject the configuration group into the form view
   automatically when
   ``_res_partner_bank_m2o_configurator_insert_form_element_ok`` is ``True``.

FAQ
---

- **Can I use this mixin on multiple models?** Yes, inherit it on any
  model that needs a configurable bank account filter.
- **Is Python code evaluation safe?** Python code is evaluated server-side
  in a restricted context; use with caution in multi-company environments.
- **Odoo version?** Odoo 15.0.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If
you spotted it first, help us smash it by providing detailed and welcomed
feedback.

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

This module is maintained by PT. Simetri Sinergi Indonesia.
