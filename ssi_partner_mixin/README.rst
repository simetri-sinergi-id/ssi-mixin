.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============
Partner Mixin
==============

Description
-----------

**Partner Mixin** is an abstract mixin module in the **@simetri-sinergi-id/ssi-mixin**
technology suite for Odoo. It provides a reusable ``mixin.partner`` abstract model that
adds configurable ``partner_id`` and ``contact_partner_id`` fields together with
view-injection hooks, so any document model can gain standardized partner and contact
handling by simply inheriting this mixin.

Key Features
------------

- **partner_id field:** ``res.partner`` field filtered to top-level partners
  (companies / individuals without a parent).
- **contact_partner_id field:** ``res.partner`` field for contact persons under
  the selected partner, filtered dynamically via computed ``allowed_contact_ids``.
- **Computed attribute flags:** Boolean fields (``mixin_partner_partner_id_required``,
  ``mixin_partner_partner_id_readonly``, ``mixin_partner_contact_id_required``,
  ``mixin_partner_contact_id_readonly``) exposing effective required/readonly state
  driven by class-level configuration and the record's current state.
- **View injection:** Optional automatic injection of partner fields into form, tree,
  and search views, controlled by class-level ``_mixin_partner_insert_*`` flags and
  ``_xpath_*`` attributes.
- **State-aware behaviour:** Required/readonly rules can be scoped to include or
  exclude specific states via ``_mixin_partner_*_include_state`` /
  ``_mixin_partner_*_exclude_state`` class attributes.

Use Cases / Context
-------------------

This mixin is suitable for any Odoo document that needs a partner relationship with
optional contact handling, such as:

- **Sales / Purchase documents:** Attach a customer or vendor and their contact person.
- **HR documents:** Link an employee's company partner and a contact representative.
- **Service requests:** Associate a partner and the specific contact that raised the
  request.
- **Custom modules:** Any custom model that requires a standardized partner + contact
  field pattern without re-implementing the logic each time.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``).
3. Update the module list (must be in developer mode).
4. Go to menu *Apps -> Apps -> Main Apps*.
5. Search for *Partner Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Install** ``ssi_partner_mixin`` via the Odoo Apps menu.
2. **Inherit** the mixin in your model::

    class MyDocument(models.Model):
        _name = "my.document"
        _inherit = ["mixin.partner", "mail.thread"]

        _mixin_partner_insert_form = True
        _mixin_partner_xpath_form = "//field[@name='name']"

3. **Configure** class-level attributes to control required/readonly rules and which
   views receive the injected fields.
4. **Use** ``partner_id`` and ``contact_partner_id`` in your business logic — the mixin
   handles domain filtering and attribute computation automatically.

FAQ
---

- **Can I use this mixin standalone?** No, it is a foundation mixin — install it as a
  dependency of your custom module.
- **Odoo version?** Odoo 15.0.
- **How do I restrict contact to a partner's contacts only?** The mixin automatically
  computes ``allowed_contact_ids`` from the selected ``partner_id``; set the
  ``contact_partner_id`` domain to ``[('id', 'in', allowed_contact_ids)]`` in your view.
- **Contribute?** Fork the repository, create a feature branch, and open a pull request
  on `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first, help us
smash it by providing detailed and welcomed feedback.

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

This module is maintained by **PT. Simetri Sinergi Indonesia**.
