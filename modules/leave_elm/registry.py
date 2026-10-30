"""What the server tells the shell about this module (ADR-0010).

Nav items carry `required_permission` and the server filters before sending —
the client does zero filtering, so a link a role cannot use never reaches the
browser at all.
"""
MODULE = {
    "code": "leave_elm", "label": "Leave Management", "icon": "Calendar",
    "base_path": "/leave", "nav_section": "Leave", "sort_order": 20,
    "status": "active",
}

NAV_ITEMS = [
    {"code": "leave.apply", "label": "Apply for Leave",
     "icon": "CheckSquare", "to": "/leave/apply",
     "required_permission": "leave_elm.apply.self",
     "sort_order": 5},
    {"code": "leave.approve", "label": "Approve Leave",
     "icon": "CheckCircle", "to": "/leave/approve",
     "required_permission": "leave_elm.approve.all",
     "sort_order": 10},
    {"code": "leave.reject", "label": "Reject Leave",
     "icon": "XCircle", "to": "/leave/reject",
     "required_permission": "leave_elm.reject.all",
     "sort_order": 15},
    {"code": "leave.cancel", "label": "Cancel Leave",
     "icon": "XSquare", "to": "/leave/cancel",
     "required_permission": "leave_elm.cancel.all",
     "sort_order": 20},
    {"code": "leave.extend", "label": "Extend Leave",
     "icon": "PlusSquare", "to": "/leave/extend",
     "required_permission": "leave_elm.extend.all",
     "sort_order": 25},
    {"code": "leave.view", "label": "View Leave",
     "icon": "Eye", "to": "/leave/view",
     "required_permission": "leave_elm.view.all",
     "sort_order": 30},
]

#: Every permission this module recognises; ROLE_GRANTS below says who holds each.
PERMISSIONS = [
    ("leave_elm.apply.self", "Apply for leave"),
    ("leave_elm.approve.all", "Approve all leave requests"),
    ("leave_elm.reject.all", "Reject all leave requests"),
    ("leave_elm.cancel.all", "Cancel all leave requests"),
    ("leave_elm.extend.all", "Extend all leave requests"),
    ("leave_elm.view.all", "View all leave requests"),
]

#: Performed by a service or a scheduled task, so no designation holds them.
SYSTEM_PERMISSIONS = [
    "leave_elm.cancel.all",
]

_STUDENT = [
    "leave_elm.apply.self",
    "leave_elm.view.all",
]

_COORDINATOR = [
    "leave_elm.apply.self",
    "leave_elm.approve.all",
    "leave_elm.reject.all",
    "leave_elm.view.all",
]

_OFFICER = [
    *_COORDINATOR,
    "leave_elm.cancel.all",
    "leave_elm.extend.all",
]

#: Oversees rather than operates: no shortlisting and no offers.
_CHAIRMAN = [
    "leave_elm.approve.all",
    "leave_elm.reject.all",
    "leave_elm.view.all",
]

#: Keyed by the designation name as it exists in globals_designation.
ROLE_GRANTS = {
    "student": _STUDENT,
    "leave_coordinator": _COORDINATOR,
    "leave_officer": _OFFICER,
    "leave_chairman": _CHAIRMAN,
    "Dean Academic": _CHAIRMAN,
}
