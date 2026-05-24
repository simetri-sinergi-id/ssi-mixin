.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

======================================
res.users Many2one Configurator Mixin
======================================

Description
-----------

``ssi_res_users_m2o_configurator_mixin`` provides an abstract Odoo model —
``mixin.res_users_m2o_configurator`` — that adds configurable filtering for
``res.users`` Many2one fields using a three-strategy pattern.

The mixin follows the same design as ``ssi_m2o_configurator_mixin`` and
integrates with ``ssi_decorator`` to optionally inject a configuration widget
into the parent model's form view.

Key Features
------------

* **Three filter strategies:** Manual (explicit user list), Domain (Odoo domain
  expression), or Python Code (custom script returning a list of user IDs).
* **Decorator-based form injection:** When
  ``_res_users_m2o_configurator_insert_form_element_ok`` is ``True``, the
  configuration group is automatically inserted into the form view at the
  XPath defined by ``_res_users_m2o_configurator_form_xpath``.
* **Reusable mixin design:** Inherit once to gain full user-selection
  configurability in any Odoo model.

Use Cases / Context
-------------------

This mixin is intended for developers building modules where users need to
configure which ``res.users`` records are selectable in a Many2one field.
Typical use cases include:

* **Approval workflows:** Restrict which users can be selected as approvers.
* **Task assignment:** Limit assignable users based on a domain or team.
* **Custom selection dialogs:** Dynamically compute available users via Python.

Installation
------------

1. Clone branch ``15.0`` of the repository
   ``https://github.com/simetri-sinergi-id/ssi-mixin``.
2. Add the path to this repository in your Odoo configuration (``addons_path``).
3. Activate developer mode and update the module list.
4. Go to *Apps → Apps → Main Apps*, search for
   *res.users Many2one Configurator Mixin*, and install it.

Installation & Usage
--------------------

After installation, inherit the mixin in your model::

    class MyModel(models.Model):
        _name = "my.model"
        _inherit = [
            "mixin.res_users_m2o_configurator",
        ]

        _res_users_m2o_configurator_insert_form_element_ok = True
        _res_users_m2o_configurator_form_xpath = "//field[@name='my_field']"

The fields ``user_selection_method``, ``user_ids``, ``user_domain``, and
``user_python_code`` are then available on your model and the configuration
widget is injected into the form view automatically.

FAQ
---

**Is this module standalone?**
  No. It is a mixin library module — install it as a dependency of your
  custom module.

**What Odoo version is supported?**
  Odoo 15.0.

**How do I select users via Python code?**
  Set ``user_selection_method`` to ``Python Code`` and write Python code in
  the ``user_python_code`` field. The code must assign a list of ``res.users``
  record IDs to the variable ``result``.

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

This module is maintained by PT. Simetri Sinergi Indonesia.
