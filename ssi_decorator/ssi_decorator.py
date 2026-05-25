# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


def attrsetter(attr, value):
    """
    Set attribute on a method for decorator pattern.
    Used internally by all decorator helpers below.
    """
    return lambda method: setattr(method, attr, value) or method


# CONFIRM
def pre_confirm_check(*args):
    """
    Decorator for pre-confirm check logic.
    Usage: decorate a method to mark it as a pre-confirm check.
    """
    return attrsetter("_pre_confirm_check", args)


def post_confirm_check(*args):
    """
    Decorator for post-confirm check logic.
    Usage: decorate a method to mark it as a post-confirm check.
    """
    return attrsetter("_post_confirm_check", args)


def pre_confirm_action(*args):
    """
    Decorator for pre-confirm action logic.
    Usage: decorate a method to mark it as a pre-confirm action.
    """
    return attrsetter("_pre_confirm_action", args)


def post_confirm_action(*args):
    """
    Decorator for post-confirm action logic.
    Usage: decorate a method to mark it as a post-confirm action.
    """
    return attrsetter("_post_confirm_action", args)


# APPROVE
def pre_approve_check(*args):
    """
    Decorator for pre-approve check logic.
    Usage: decorate a method to mark it as a pre-approve check.
    """
    return attrsetter("_pre_approve_check", args)


def post_approve_check(*args):
    """
    Decorator for post-approve check logic.
    Usage: decorate a method to mark it as a post-approve check.
    """
    return attrsetter("_post_approve_check", args)


def pre_approve_action(*args):
    """
    Decorator for pre-approve action logic.
    Usage: decorate a method to mark it as a pre-approve action.
    """
    return attrsetter("_pre_approve_action", args)


def post_approve_action(*args):
    """
    Decorator for post-approve action logic.
    Usage: decorate a method to mark it as a post-approve action.
    """
    return attrsetter("_post_approve_action", args)


# REJECT
def pre_reject_check(*args):
    """
    Decorator for pre-reject check logic.
    Usage: decorate a method to mark it as a pre-reject check.
    """
    return attrsetter("_pre_reject_check", args)


def post_reject_check(*args):
    """
    Decorator for post-reject check logic.
    Usage: decorate a method to mark it as a post-reject check.
    """
    return attrsetter("_post_reject_check", args)


def pre_reject_action(*args):
    """
    Decorator for pre-reject action logic.
    Usage: decorate a method to mark it as a pre-reject action.
    """
    return attrsetter("_pre_reject_action", args)


def post_reject_action(*args):
    """
    Decorator for post-reject action logic.
    Usage: decorate a method to mark it as a post-reject action.
    """
    return attrsetter("_post_reject_action", args)


# OPEN
def pre_open_check(*args):
    """
    Decorator for pre-open check logic.
    Usage: decorate a method to mark it as a pre-open check.
    """
    return attrsetter("_pre_open_check", args)


def post_open_check(*args):
    """
    Decorator for post-open check logic.
    Usage: decorate a method to mark it as a post-open check.
    """
    return attrsetter("_post_open_check", args)


def pre_open_action(*args):
    """
    Decorator for pre-open action logic.
    Usage: decorate a method to mark it as a pre-open action.
    """
    return attrsetter("_pre_open_action", args)


def post_open_action(*args):
    """
    Decorator for post-open action logic.
    Usage: decorate a method to mark it as a post-open action.
    """
    return attrsetter("_post_open_action", args)


# READY
def pre_ready_check(*args):
    """
    Decorator for pre-ready check logic.
    Usage: decorate a method to mark it as a pre-ready check.
    """
    return attrsetter("_pre_ready_check", args)


def post_ready_check(*args):
    """
    Decorator for post-ready check logic.
    Usage: decorate a method to mark it as a post-ready check.
    """
    return attrsetter("_post_ready_check", args)


def pre_ready_action(*args):
    """
    Decorator for pre-ready action logic.
    Usage: decorate a method to mark it as a pre-ready action.
    """
    return attrsetter("_pre_ready_action", args)


def post_ready_action(*args):
    """
    Decorator for post-ready action logic.
    Usage: decorate a method to mark it as a post-ready action.
    """
    return attrsetter("_post_ready_action", args)


# QUEUE TO DONE
def pre_queue_done_check(*args):
    """
    Decorator for pre-queue-to-done check logic.
    Usage: decorate a method to mark it as a pre-queue-to-done check.
    """
    return attrsetter("_pre_queue_done_check", args)


def post_queue_done_check(*args):
    """
    Decorator for post-queue-to-done check logic.
    Usage: decorate a method to mark it as a post-queue-to-done check.
    """
    return attrsetter("_post_queue_done_check", args)


def pre_queue_done_action(*args):
    """
    Decorator for pre-queue-to-done action logic.
    Usage: decorate a method to mark it as a pre-queue-to-done action.
    """
    return attrsetter("_pre_queue_done_action", args)


def post_queue_done_action(*args):
    """
    Decorator for post-queue-to-done action logic.
    Usage: decorate a method to mark it as a post-queue-to-done action.
    """
    return attrsetter("_post_queue_done_action", args)


# DONE
def pre_done_check(*args):
    """
    Decorator for pre-done check logic.
    Usage: decorate a method to mark it as a pre-done check.
    """
    return attrsetter("_pre_done_check", args)


def post_done_check(*args):
    """
    Decorator for post-done check logic.
    Usage: decorate a method to mark it as a post-done check.
    """
    return attrsetter("_post_done_check", args)


def pre_done_action(*args):
    """
    Decorator for pre-done action logic.
    Usage: decorate a method to mark it as a pre-done action.
    """
    return attrsetter("_pre_done_action", args)


def post_done_action(*args):
    """
    Decorator for post-done action logic.
    Usage: decorate a method to mark it as a post-done action.
    """
    return attrsetter("_post_done_action", args)


# QUEUE TO CANCEL
def pre_queue_cancel_check(*args):
    """
    Decorator for pre-queue-to-cancel check logic.
    Usage: decorate a method to mark it as a pre-queue-to-cancel check.
    """
    return attrsetter("_pre_queue_cancel_check", args)


def post_queue_cancel_check(*args):
    """
    Decorator for post-queue-to-cancel check logic.
    Usage: decorate a method to mark it as a post-queue-to-cancel check.
    """
    return attrsetter("_post_queue_cancel_check", args)


def pre_queue_cancel_action(*args):
    """
    Decorator for pre-queue-to-cancel action logic.
    Usage: decorate a method to mark it as a pre-queue-to-cancel action.
    """
    return attrsetter("_pre_queue_cancel_action", args)


def post_queue_cancel_action(*args):
    """
    Decorator for post-queue-to-cancel action logic.
    Usage: decorate a method to mark it as a post-queue-to-cancel action.
    """
    return attrsetter("_post_queue_cancel_action", args)


# CANCEL
def pre_cancel_check(*args):
    """
    Decorator for pre-cancel check logic.
    Usage: decorate a method to mark it as a pre-cancel check.
    """
    return attrsetter("_pre_cancel_check", args)


def post_cancel_check(*args):
    """
    Decorator for post-cancel check logic.
    Usage: decorate a method to mark it as a post-cancel check.
    """
    return attrsetter("_post_cancel_check", args)


def pre_cancel_action(*args):
    """
    Decorator for pre-cancel action logic.
    Usage: decorate a method to mark it as a pre-cancel action.
    """
    return attrsetter("_pre_cancel_action", args)


def post_cancel_action(*args):
    """
    Decorator for post-cancel action logic.
    Usage: decorate a method to mark it as a post-cancel action.
    """
    return attrsetter("_post_cancel_action", args)


# RESTART
def pre_restart_check(*args):
    """
    Decorator for pre-restart check logic.
    Usage: decorate a method to mark it as a pre-restart check.
    """
    return attrsetter("_pre_restart_check", args)


def post_restart_check(*args):
    """
    Decorator for post-restart check logic.
    Usage: decorate a method to mark it as a post-restart check.
    """
    return attrsetter("_post_restart_check", args)


def pre_restart_action(*args):
    """
    Decorator for pre-restart action logic.
    Usage: decorate a method to mark it as a pre-restart action.
    """
    return attrsetter("_pre_restart_action", args)


def post_restart_action(*args):
    """
    Decorator for post-restart action logic.
    Usage: decorate a method to mark it as a post-restart action.
    """
    return attrsetter("_post_restart_action", args)


# TERMINATE
def pre_terminate_check(*args):
    """
    Decorator for pre-terminate check logic.
    Usage: decorate a method to mark it as a pre-terminate check.
    """
    return attrsetter("_pre_terminate_check", args)


def post_terminate_check(*args):
    """
    Decorator for post-terminate check logic.
    Usage: decorate a method to mark it as a post-terminate check.
    """
    return attrsetter("_post_terminate_check", args)


def pre_terminate_action(*args):
    """
    Decorator for pre-terminate action logic.
    Usage: decorate a method to mark it as a pre-terminate action.
    """
    return attrsetter("_pre_terminate_action", args)


def post_terminate_action(*args):
    """
    Decorator for post-terminate action logic.
    Usage: decorate a method to mark it as a post-terminate action.
    """
    return attrsetter("_post_terminate_action", args)


# WIN
def pre_win_check(*args):
    """
    Decorator for pre-win check logic.
    Usage: decorate a method to mark it as a pre-win check.
    """
    return attrsetter("_pre_win_check", args)


def post_win_check(*args):
    """
    Decorator for post-win check logic.
    Usage: decorate a method to mark it as a post-win check.
    """
    return attrsetter("_post_win_check", args)


def pre_win_action(*args):
    """
    Decorator for pre-win action logic.
    Usage: decorate a method to mark it as a pre-win action.
    """
    return attrsetter("_pre_win_action", args)


def post_win_action(*args):
    """
    Decorator for post-win action logic.
    Usage: decorate a method to mark it as a post-win action.
    """
    return attrsetter("_post_win_action", args)


# LOST
def pre_lost_check(*args):
    """
    Decorator for pre-lost check logic.
    Usage: decorate a method to mark it as a pre-lost check.
    """
    return attrsetter("_pre_lost_check", args)


def post_lost_check(*args):
    """
    Decorator for post-lost check logic.
    Usage: decorate a method to mark it as a post-lost check.
    """
    return attrsetter("_post_lost_check", args)


def pre_lost_action(*args):
    """
    Decorator for pre-lost action logic.
    Usage: decorate a method to mark it as a pre-lost action.
    """
    return attrsetter("_pre_lost_action", args)


def post_lost_action(*args):
    """
    Decorator for post-lost action logic.
    Usage: decorate a method to mark it as a post-lost action.
    """
    return attrsetter("_post_lost_action", args)


# fields_view_get
def insert_on_tree_view(*args):
    """
    Decorator for tree view injection logic.
    Usage: decorate a method to mark it for tree view element injection.
    """
    return attrsetter("_insert_on_tree_view", args)


def insert_on_form_view(*args):
    """
    Decorator for form view injection logic.
    Usage: decorate a method to mark it for form view element injection.
    """
    return attrsetter("_insert_on_form_view", args)


def insert_on_search_view(*args):
    """
    Decorator for search view injection logic.
    Usage: decorate a method to mark it for search view element injection.
    """
    return attrsetter("_insert_on_search_view", args)
