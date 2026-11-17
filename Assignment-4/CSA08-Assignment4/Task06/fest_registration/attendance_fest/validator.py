import re

class InvalidRegistration(Exception):
    """A registration row is malformed or contains invalid data."""

def parse_registration(line):
    fields = [part.strip() for part in line.split(",")]
    if len(fields) != 5:
        raise InvalidRegistration(f"expected 5 fields, found {len(fields)}")
    reg_no, name, department, email, events_text = fields
    if not reg_no or not name or not department:
        raise InvalidRegistration("register number, name and department are required")
    # Simple string-method validation as requested: exactly one @ and a dot after it.
    if email.count("@") != 1:
        raise InvalidRegistration(f"invalid email '{email}'")
    local, domain = email.split("@")
    if not local or "." not in domain or domain.startswith(".") or domain.endswith("."):
        raise InvalidRegistration(f"invalid email '{email}'")
    events = [event.strip() for event in events_text.split(";") if event.strip()]
    if not events:
        raise InvalidRegistration("at least one event is required")
    return {
        "register_number": reg_no,
        "name": name,
        "department": department,
        "email": email,
        "events": events,
    }
