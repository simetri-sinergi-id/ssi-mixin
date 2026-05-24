.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================================
Custom Date Field With Callable Attribute
=========================================

Description
-----------

``ssi_field_date_callable_attribute`` provides a custom Odoo field class
— ``DateCallable`` (exposed as ``fields.DateCallable``) — that extends
``fields.Date`` to accept callable values for the ``readonly``,
``required``, ``string``, and ``states`` attributes.

This allows those attributes to be set to ``@api.model`` methods on the
model class so that subclasses can fully customise the field's behaviour
through class-level attribute overrides without redeclaring the field.

The field is primarily used by ``ssi_duration_mixin`` to provide fully
configurable ``date_start`` / ``date_end`` fields.

Key Features
------------

- **Callable Attributes:** ``readonly``, ``required``, ``string``, and
  ``states`` can be set to callable model methods.
- **Mixin-Friendly:** Enables subclasses to override field behaviour via
  class-level attribute overrides without redeclaring the field.
- **Drop-in Replacement:** ``fields.DateCallable`` is a direct subclass of
  ``fields.Date`` and behaves identically when no callable is used.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

- **Duration Mixin:** Provides configurable ``date_start`` / ``date_end``
  fields in ``ssi_duration_mixin``.
- **Custom Modules:** Any module requiring dynamic field attribute resolution
  at setup time based on model-level methods.

Installation
------------

1. Clone the branch **15.0** of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration
   (``addons-path``)
3. Update the module list (ensure you are in developer mode)
4. Go to menu *Apps → Apps → Main Apps*
5. Search for *Custom Date Field With Callable Attribute*
6. Install the module

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_field_date_callable_attribute`` in your
   Odoo addons path.
2. **Enable:** In Odoo Apps, search for
   ``ssi_field_date_callable_attribute`` and install.
3. **Use:** Declare a ``fields.DateCallable`` on your model and set
   ``readonly``, ``required``, ``string``, or ``states`` to an
   ``@api.model`` method. The callable will be evaluated once at
   field-setup time.

FAQ
---

- **Standalone?** Yes, but it is primarily intended as a dependency for
  ``ssi_duration_mixin`` and similar mixin modules.
- **Odoo Version?** Odoo 15.0 or above.
- **Contribute?** Fork, branch, and submit a pull request on
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

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
