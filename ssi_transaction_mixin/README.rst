=================
Transaction Mixin
=================

Description
-----------

**Transaction Mixin** is a core mixin module in the **@simetri-sinergi-id/ssi-mixin**
technology suite for Odoo 15. It provides the foundational abstract model —
``mixin.transaction`` — used by all SSI transactional documents.

It composes the following base capabilities:

- **mail.thread** / **mail.activity.mixin** — chatter and activity tracking.
- **mixin.decorator** — form-view injection framework.
- **mixin.sequence** — auto-generated document number.
- **mixin.policy** — policy-template-driven button visibility.
- **mixin.print_document** — print/download actions.

And adds:

- A ``name`` (document number) field with configurable draft sequence state.
- ``company_id``, ``user_id``, and ``reviewer_id`` standard header fields.
- Automatic form-view injection of status bar, policy fields, and action buttons.
- ``action_restart`` lifecycle action with pre/post hooks via decorator pattern.
- Duplicate document-number constraint with bypass support.
- Safe ``unlink`` guard that prevents deletion outside draft state.

Key Features
------------

- **Abstract Mixin Design:** Inherit ``mixin.transaction`` in any transactional model with zero structural view duplication.
- **Auto Document Number:** Configurable sequence-based document numbering via ``mixin.sequence``.
- **Restart Action:** Built-in restart lifecycle with pre/post hook points using the decorator pattern.
- **Policy-Driven Buttons:** Button visibility is controlled by a policy template — no hard-coded domain logic.
- **Duplicate Number Guard:** Constraint prevents duplicate document numbers across records of the same model.
- **Chatter & Activities:** Full messaging thread and activity scheduling on every inheriting model.
- **Safe Delete:** Prevents unlink unless the document is in draft state and number is ``/``.
- **Open Source:** AGPL-3.0 license with community-driven improvements.

Use Cases / Context
-------------------

Use this mixin as the foundation for any transactional document that needs a workflow lifecycle:

- **Purchase Orders / Sales Orders:** Standardise transaction lifecycle and document numbering.
- **Internal Requests:** HR requests, IT requests, or any approval-based internal document.
- **Warehouse Transfers:** Stock movement documents with configurable approval states.
- **Financial Documents:** Journal entries, payment requests, or any finance-related transaction.
- **Custom Workflows:** Any document that requires draft → confirmed → done → cancelled states.

Simply set ``_inherit = ["mixin.transaction"]`` on your model and extend the state selection
and lifecycle hooks according to your business needs.

Installation
------------

1. Clone branch **15.0** of the repository: https://github.com/simetri-sinergi-id/ssi-mixin
2. Add the path to this repository in your Odoo configuration (``addons-path``).
3. Update the module list (ensure you are in developer mode).
4. Go to menu *Apps → Apps → Main Apps*.
5. Search for *Transaction Mixin*.
6. Install the module.

Installation & Usage
--------------------

1. **Add to Odoo:** Place ``ssi_transaction_mixin`` in your Odoo addons path.
2. **Enable:** In Odoo Apps, search for ``ssi_transaction_mixin`` and install.
3. **Extend:** In your custom model, add ``_inherit = ["mixin.transaction"]``.
4. **Add States:** Extend the ``state`` field selection with your required workflow states.
5. **Add Hooks:** Implement pre/post hooks via the decorator pattern to add business logic
   without overriding core methods.

FAQ
---

- **Standalone?** No — it is a mixin foundation. Install it as a dependency of your custom transactional module.
- **Odoo Version?** Odoo 15.0.
- **How do I add more states?** Extend the ``state`` field in your concrete model and add sub-mixins such as ``mixin.transaction.confirm`` or ``mixin.transaction.done``.
- **Can I disable the restart button?** Set ``_automatically_insert_restart_button = False`` on your model class.
- **Contribute?** Fork, branch, and submit a pull request on `GitHub <https://github.com/simetri-sinergi-id/ssi-mixin>`_.

Bug Tracker
-----------

Bugs are tracked on `GitHub Issues <https://github.com/simetri-sinergi-id/ssi-mixin/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us smash it by providing detailed and welcomed feedback.

Credits
-------

Contributors
~~~~~~~~~~~~

- Andhitia Rama <andhitia.r@gmail.com>
- Miftahussalam <miftahussalam08@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by PT. Simetri Sinergi Indonesia.
