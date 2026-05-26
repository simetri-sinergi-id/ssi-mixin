.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
    :target: https://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

============
Policy Mixin
============

Description
-----------
Policy Mixin is a core mixin module for Odoo 18.0, providing standardized policy and workflow management capabilities that can be integrated into other modules. It enables flexible, reusable policy templates and detail configurations for business process control.

Key Features
------------
- Reusable policy template model
- Detail configuration for field-level policy
- Company and model-specific policy support
- State-based restriction and validation
- Extensible for custom business logic

Use Cases / Context
-------------------
Use this module to enforce workflow policies, restrict field access, or implement business rules that depend on model state or company context. Suitable for organizations needing flexible, maintainable policy management in Odoo.

Installation
------------
1. Clone the repository and add to your Odoo addons path.
2. Update the app list and install "Policy Mixin" from Apps menu.

Installation & Usage
--------------------
After installation, configure policy templates and details from the Policy menu. Integrate with other modules by inheriting the mixin or referencing policy templates in your business logic.

FAQ
---
- **Q:** Can I use this for any model?
   **A:** Yes, as long as you configure the template for the target model.
- **Q:** How to add custom logic?
   **A:** Inherit the mixin and override methods as needed.

Bug Tracker
-----------
Bugs are tracked on `GitHub Issues <https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_. Please report with details for faster resolution.

Credits
-------
- Michael Viriyananda
- Andhitia Rama

Maintainer
----------
PT. Simetri Sinergi Indonesia
------------------------------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
