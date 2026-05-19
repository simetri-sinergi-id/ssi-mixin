.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

==============================
Test Module: Transaction Mixin
==============================

Description
===========

Test Module: Transaction Mixin is a test module for validating the behaviour
of the transaction mixin within the SSI ecosystem. It leverages various
transaction workflow mixins (confirm, open, done, cancel, terminate) to ensure
that decorator hooks, approvals, and status flows work as expected.

Key Features
============

* Testing the transaction state flow from draft to terminate.
* Testing pre/post decorator hooks on actions and checks.
* Integration with approval policy and sequence templates.
* Example transaction with detail lines and product price computation.

Use Cases / Context
===================

* Used as a reference module when developing new transaction mixins.
* Helps with regression testing for changes to ``ssi_transaction_*_mixin`` modules.
* Serves as an implementation example for inheriting from transaction mixin models.

Installation
============

1. Clone the 15.0 branch of the repository:
   https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the repository path to your Odoo configuration (``addons-path``).
3. Update the module list in developer mode.
4. Open the menu *Apps -> Apps -> Main Apps*.
5. Search for *Test Module: Transaction Mixin*.
6. Install the module.

Installation & Usage
====================

1. Make sure the SSI transaction mixin module dependencies are available.
2. Install the ``test_ssi_transaction_mixin`` module from Apps.
3. Create test transaction records and run the confirm/open/done/cancel actions
   to verify pre/post hooks.
4. Use the form view to inspect the check/action marker fields that are
   automatically populated by the decorator.

FAQ
===

* **Is this module intended for production use?**
  No, this module is intended for testing and validating mixin behaviour.
* **Which Odoo version is supported?**
  This module targets Odoo 15.0.
* **How can I contribute?**
  Fork the repository, make your changes in a separate branch, then submit
  a pull request to the GitHub repository.

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. In case of trouble,
please check there if your issue has already been reported. If you spotted it
first, help us improve by providing detailed feedback.

Credits
=======

Contributors
------------

* Michael Viriyananda <viriyananda.michael@gmail.com>
* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
==========

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://github.com/simetri-sinergi-id

This module is maintained by PT. Simetri Sinergi Indonesia.
