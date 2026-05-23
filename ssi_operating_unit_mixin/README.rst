.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

====================
Operating Unit Mixin
====================

Description
-----------

**Operating Unit Mixin** is a core mixin module in the
``@simetri-sinergi-id/ssi-mixin`` technology suite for Odoo 15.
It provides two abstract models that add operating-unit awareness to any
model, enabling granular access control and data segregation by operating
unit across documents and sequences.

Key Features
------------

- **Single Operating Unit:** ``mixin.single_operating_unit`` adds an
  ``operating_unit_id`` Many2one field, defaulting to the current user's
  default operating unit.
- **Multiple Operating Units:** ``mixin.multiple_operating_unit`` adds an
  ``operating_unit_ids`` Many2many field for records that can span multiple
  operating units simultaneously.
- **Sequence Scoping:** Extends ``ir.sequence`` with operating-unit
  awareness so sequences can be restricted to specific operating units.
- **IR Rule Integration:** Includes a domain rule ensuring users only see
  sequences belonging to their operating units.
- **Mixin Design:** Zero-intrusion — inherit either mixin in any model to
  get full operating-unit capability.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

- **Multi-Branch Operations:** Restrict documents and sequences to specific
  branches or business units.
- **Access Control:** Ensure users only interact with data relevant to their
  operating unit.
- **Custom Transactional Models:** Any model that needs to be scoped by
  operating unit.
- **Sequence Management:** Automatically filter ``ir.sequence`` records by
  the user's operating units.

Installation
------------

To install this module, you need to:

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Operating Unit Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_operating_unit_mixin`` in your Odoo addons
   path alongside the ``operating_unit`` module.
2. **Enable:** In Odoo Apps, search for *Operating Unit Mixin* and install.
3. **Extend (single OU):** Inherit ``mixin.single_operating_unit`` in your
   model to add the ``operating_unit_id`` field.
4. **Extend (multiple OUs):** Inherit ``mixin.multiple_operating_unit`` in
   your model to add the ``operating_unit_ids`` field.
5. **Sequences:** The module automatically scopes ``ir.sequence`` records to
   the current user's operating units via an IR rule.

FAQ
---

- **Is this module standalone?**
  No. It requires the ``operating_unit`` module to be installed first.
- **Odoo Version?**
  Odoo 15.0.
- **Can a model use both mixins?**
  No — choose either ``mixin.single_operating_unit`` (one OU per record) or
  ``mixin.multiple_operating_unit`` (many OUs per record) depending on your
  use case.
- **Contribute?**
  Fork, branch, and submit a pull request on
  `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed
feedback.

Credits
-------

Contributors
~~~~~~~~~~~~

* Michael Viriyananda <viriyananda.michael@gmail.com>
* Andhitia Rama <andhitia.r@gmail.com>
* Asrul Bastian Yunas <asrulbastianyunas@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
