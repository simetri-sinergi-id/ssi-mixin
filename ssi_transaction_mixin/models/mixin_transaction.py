# Copyright 2026 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl-3.0.html).

from inspect import getmembers

from lxml import etree

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class MixinTransaction(models.AbstractModel):
    """
    Abstract model to transaction object
    """

    _name = "mixin.transaction"
    _inherit = [
        "mail.activity.mixin",
        "mail.thread",
        "mixin.decorator",
        "mixin.sequence",
        "mixin.policy",
        "mixin.print_document",
    ]
    _description = "Transaction Mixin"
    _draft_state = "draft"
    _create_sequence_state = False
    _document_number_field = "name"
    _automatically_insert_view_element = False
    _automatically_insert_print_button = True
    _automatically_insert_restart_button = True

    _automatically_reconfigure_statusbar_visible = True
    _policy_field_order = False
    _header_button_order = False

    _statusbar_visible_label = "draft"
    _policy_field_xpath = (
        "/form/sheet/notebook/page[@name='policy']"
        "/group[@name='policy_2']/field[@name='restart_ok']"
    )

    # Attributes related to add element on search view automatically
    _state_filter_xpath = "/search/group[@name='dom_state']/filter[@name='dom_draft']"
    _state_filter_order = False

    name = fields.Char(
        string="Document Name",
        default="/",
        required=True,
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Transaction/document number.\n\n"
        "* Unique identifier of transaction\n"
        "* Leave '/' to automatically generate number\n"
        "* Change '/' into any number/identifier to manually assign number.\n"
        "  Manual number assignment can be done in 'Draft' state\n"
        "  Only user with 'Can Manually Assign Number' policy"
        " can manually assign number.\n"
        "* Transaction with number other than '/' can not be deleted.",
        translate=True,
    )

    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        required=True,
        default=lambda self: self._default_company_id(),
        copy=True,
        help="Company that owns the document.\n\n"
        "* Automatically filled with user's company.\n"
        "  Default company can be changed.",
        translate=True,
    )
    company_partner_id = fields.Many2one(
        string="Company Partner",
        related="company_id.partner_id",
        store=False,
    )

    user_id = fields.Many2one(
        string="Responsible",
        comodel_name="res.users",
        required=True,
        default=lambda self: self._default_user_id(),
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="User responsible for document.\n\n"
        "* Creator can be different from responsible user.\n"
        "* Automatically filled with user that initiates document creation.\n"
        "  Default responsible can be changed.",
        translate=True,
    )
    reviewer_id = fields.Many2one(
        string="Reviewer",
        comodel_name="res.users",
        required=False,
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="User responsible to review document.\n\n"
        "* Unless configured to approve, reviewer does not equal to approver.",
        translate=True,
    )

    note = fields.Text(
        string="Note",
        copy=True,
        help="Additional notes for this transaction.",
        translate=True,
    )
    state = fields.Selection(
        string="State",
        selection=[
            ("draft", "Draft"),
        ],
        default="draft",
        required=True,
        copy=False,
        readonly=True,
        states={"draft": [("readonly", False)]},
        help="Current state of the transaction.",
        translate=True,
    )

    restart_ok = fields.Boolean(
        string="Can Restart",
        compute="_compute_policy",
        compute_sudo=True,
        help=(
            "Restart policy.\n\n"
            "* If active user can see and execute 'Restart' button."
        ),
        translate=True,
    )
    manual_number_ok = fields.Boolean(
        string="Can Input Manual Document Number",
        compute="_compute_policy",
        compute_sudo=True,
        help=(
            "Manual number assignment policy.\n\n"
            "* If active user can edit document number."
        ),
        translate=True,
    )
    display_name = fields.Char(
        string="Display Name",
        compute="_compute_display_name",
        store=True,
        index=True,
        help="Display name for the transaction.",
        translate=True,
    )

    @api.depends(lambda self: [self._document_number_field])
    def _compute_display_name(self):
        """
        Compute the display name for each record based on the document number field.
        """
        names = dict(self.name_get())
        for rec in self:
            rec.display_name = names.get(rec.id)

    @api.model
    def _default_company_id(self):
        """
        Return the default company ID for the current user.
        """
        return self.env.user.company_id.id

    @api.model
    def _default_user_id(self):
        """
        Return the default user ID for the current user.
        """
        return self.env.user.id

    def _compute_policy(self):
        """
        Compute policy-related fields by calling the super method.
        """
        _super = super()
        _super._compute_policy()

    # TODO: Dynamic field name
    @api.constrains(
        "name",
    )
    def _constrains_duplicate_document_number(self):
        """
        Constraint: Prevent duplicate document number.
        Raises UserError if a duplicate is found.
        """
        for record in self.sudo():
            if not record._check_duplicate_document_number():
                error_message = (
                    f"Document Type: {self._description.lower()}\n"
                    f"Context: Change document number\n"
                    f"Database ID: {record.id}\n"
                    f"Problem: Duplicate document number\n"
                    f"Solution: Change document number into different number"
                )
                raise UserError(_(error_message))

    def name_get(self):
        """
        Return display name for each record.

        If the document number is '/', use '*id' as the name,
        otherwise use the document name.
        """
        result = []
        for record in self:
            if getattr(record, self._document_number_field) == "/":
                name = f"*{record.id}"
            else:
                name = record.name
            result.append((record.id, name))
        return result

    def unlink(self):
        """
        Override unlink to prevent deleting non-draft or numbered documents.
        Raises UserError if the document is not in draft state or has a manual number.
        """
        force_unlink = self.env.context.get("ssi_transaction_mixin_force_unlink", False)
        for record in self:
            if not record._check_state_unlink(force_unlink):
                error_message = (
                    f"Document Type: {self._description.lower()}\n"
                    f"Context: Delete document\n"
                    f"Database ID: {record.id}\n"
                    f"Problem: Document state is not draft\n"
                    f"Solution: Cancel and restart document"
                )
                raise UserError(_(error_message))
            if not record._check_document_number_unlink(force_unlink):
                error_message = (
                    f"Document Type: {self._description.lower()}\n"
                    f"Context: Delete document\n"
                    f"Database ID: {record.id}\n"
                    f"Problem: Document number is not equal to /\n"
                    f"Solution: Change document number into /"
                )
                raise UserError(_(error_message))
        return super().unlink()

    @api.model
    def fields_view_get(
        self, view_id=None, view_type="form", toolbar=False, submenu=False
    ):
        """
        Override to allow dynamic view element injection for form and search views.
        Reorders header buttons, policy fields, and state filters if enabled.
        """
        result = super().fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu
        )
        View = self.env["ir.ui.view"]

        view_arch = etree.XML(result["arch"])

        if view_type == "form" and self._automatically_insert_view_element:
            view_arch = self._reorder_header_button(view_arch)
            view_arch = self._reorder_policy_field(view_arch)
        elif view_type == "search" and self._automatically_insert_view_element:
            view_arch = self._reorder_state_filter_on_search_view(view_arch)

        if view_id and result.get("base_model", self._name) != self._name:
            View = View.with_context(base_model_name=result["base_model"])
        new_arch, new_fields = View.postprocess_and_fields(view_arch, self._name)
        result["arch"] = new_arch
        new_fields.update(result["fields"])
        result["fields"] = new_fields

        return result

    def action_restart(self):
        """
        Restart the transaction by running pre/post checks and actions,
        updating state, and notifying.
        """
        for record in self.sudo():
            record._check_restart_policy()
            record._run_pre_restart_check()
            record._run_pre_restart_action()
            record.write(record._prepare_restart_data())
            record._run_post_restart_check()
            record._run_post_restart_action()
            record._notify_restart_action()

    def action_reset_document_number(self):
        """
        Reset the document number to '/' after checking policy.
        """
        for record in self.sudo():
            record._check_reset_number_policy()
            record._reset_document_number()

    def _reset_document_number(self):
        """
        Reset the document number to '/'.
        """
        self.ensure_one()
        self.write(
            {
                "name": "/",
            }
        )

    def _check_reset_number_policy(self):
        """
        Check if the user is allowed to reset the document number.
        Raises UserError if not allowed.
        """
        self.ensure_one()

        if self.env.context.get("bypass_policy_check", False):
            return True

        if not self.manual_number_ok:
            error_message = (
                f"Document Type: {self._description}\n"
                f"Context: Reset document number\n"
                f"Database ID: {self.id}\n"
                f"Problem: Reset document is not allowed\n"
                f"Solution: Check restart policy prerequisite"
            )
            raise UserError(_(error_message))

    def _notify_restart_action(self):
        """
        Post a notification message after restart action.
        """
        self.ensure_one()
        msg = self._prepare_restart_action_notification()
        self.message_post(
            body=_(msg), message_type="notification", subtype_xmlid="mail.mt_note"
        )

    def _prepare_restart_action_notification(self):
        """
        Prepare the notification message for restart action.
        """
        self.ensure_one()
        # Notifikasi restart, gunakan f-string dan _()
        return _("{doc} {name} restarted").format(
            doc=self._description, name=self.display_name
        )

    def _check_restart_policy(self):
        """
        Check if the document can be restarted according to policy.
        Raises UserError if not allowed.
        """
        self.ensure_one()

        if not self._automatically_insert_restart_button:
            return True

        if self.env.context.get("bypass_policy_check", False):
            return True

        if not self.restart_ok:
            error_message = (
                f"Document Type: {self._description.lower()}\n"
                f"Context: Restart document\n"
                f"Database ID: {self.id}\n"
                f"Problem: Document is not allowed to restart\n"
                f"Solution: Check restart policy prerequisite"
            )
            raise UserError(_(error_message))

    def _run_pre_restart_check(self):
        """
        Run all decorator methods for pre-restart checks.
        """
        self.ensure_one()
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_decorator(func, "_pre_restart_check"):
                methods.append(func)
        if methods:
            self.run_decorator_method(methods)

    def _run_post_restart_check(self):
        """
        Run all decorator methods for post-restart checks.
        """
        self.ensure_one()
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_decorator(func, "_post_restart_check"):
                methods.append(func)
        if methods:
            self.run_decorator_method(methods)

    def _run_pre_restart_action(self):
        """
        Run all decorator methods for pre-restart actions.
        """
        self.ensure_one()
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_decorator(func, "_pre_restart_action"):
                methods.append(func)
        if methods:
            self.run_decorator_method(methods)

    def _run_post_restart_action(self):
        """
        Run all decorator methods for post-restart actions.
        """
        self.ensure_one()
        cls = type(self)
        methods = []
        for _attr, func in getmembers(cls):
            if self.is_decorator(func, "_post_restart_action"):
                methods.append(func)
        if methods:
            self.run_decorator_method(methods)

    def _prepare_restart_data(self):
        """
        Prepare the data dictionary for restarting the transaction (set state to draft).
        """
        self.ensure_one()
        return {
            "state": self._draft_state,
        }

    def _check_document_number_unlink(self, force_unlink=False):
        """
        Check if the document number allows unlink (must be '/' or force_unlink).
        Returns True if allowed, False otherwise.
        """
        self.ensure_one()
        result = True
        if getattr(self, self._document_number_field) != "/" and not force_unlink:
            result = False
        return result

    def _check_state_unlink(self, force_unlink=False):
        """
        Check if the state allows unlink (must be 'draft' or force_unlink).
        Returns True if allowed, False otherwise.
        """
        self.ensure_one()
        result = True
        if self.state != "draft" and not force_unlink:
            result = False
        return result

    def _check_duplicate_document_number(self):
        """
        Check for duplicate document number in the database.
        Returns True if no duplicate, False otherwise.
        """
        self.ensure_one()
        result = True
        criteria = [
            (
                self._document_number_field,
                "=",
                getattr(self, self._document_number_field),
            ),
            (self._document_number_field, "!=", "/"),
            ("id", "!=", self.id),
        ]
        ObjectMixin = self.env[self._name]
        count_duplicate = ObjectMixin.search_count(criteria)
        if count_duplicate > 0:
            result = False
        return result

    @api.model
    def _reorder_header_button(self, view_arch):
        """
        Reorder header buttons in the form view according to _header_button_order.
        """
        if not self._header_button_order:
            return view_arch
        _xpath = "/form/header"
        if len(view_arch.xpath(_xpath)) == 0:
            return view_arch
        node_xpath = view_arch.xpath(_xpath)[0]
        for node in node_xpath:
            if node.get("name") in self._header_button_order:
                node.set(
                    "order", str(self._header_button_order.index(node.get("name")))
                )
        to_sort = (e for e in node_xpath if e.tag == "button")
        no_sort = (e for e in node_xpath if e.tag == "field")
        node_xpath[:] = sorted(
            to_sort, key=lambda child: int(child.get("order", "100"))
        ) + list(no_sort)
        return view_arch

    @api.model
    def _reorder_policy_field(self, view_arch):
        """
        Reorder policy fields in the form view according to _policy_field_order.
        """
        if not self._policy_field_order:
            return view_arch
        _xpath = "/form/sheet/notebook/page[@name='policy']/group[@name='policy_2']"
        if len(view_arch.xpath(_xpath)) == 0:
            return view_arch
        node_xpath = view_arch.xpath(_xpath)[0]
        for node in node_xpath:
            if node.get("name") in self._policy_field_order:
                node.set("order", str(self._policy_field_order.index(node.get("name"))))
        to_sort = (e for e in node_xpath if e.tag == "field")
        node_xpath[:] = sorted(
            to_sort, key=lambda child: int(child.get("order", "100"))
        )
        return view_arch

    @api.model
    def _reconfigure_statusbar_visible(self, view_arch):
        """
        Set the statusbar_visible attribute for the state field in the form header.
        """
        if not self._automatically_reconfigure_statusbar_visible:
            return view_arch
        _xpath = "/form/header/field[@name='state']"
        if len(view_arch.xpath(_xpath)) == 0:
            return view_arch
        node_xpath = view_arch.xpath(_xpath)[0]
        node_xpath.set("statusbar_visible", self._statusbar_visible_label)
        return view_arch

    @api.model
    def _reorder_state_filter_on_search_view(self, view_arch):
        """
        Reorder state filters in the search view according to _state_filter_order.
        """
        if not self._state_filter_order:
            return view_arch
        _xpath = "/search/group[@name='dom_state']"  # TODO: Make it as class attribute
        if len(view_arch.xpath(_xpath)) == 0:
            return view_arch
        node_xpath = view_arch.xpath(_xpath)[0]
        for node in node_xpath:
            if node.get("name") in self._state_filter_order:
                node.set("order", str(self._state_filter_order.index(node.get("name"))))
        to_sort = (e for e in node_xpath if e.tag == "filter")
        node_xpath[:] = sorted(
            to_sort, key=lambda child: int(child.get("order", "100"))
        )
        return view_arch
