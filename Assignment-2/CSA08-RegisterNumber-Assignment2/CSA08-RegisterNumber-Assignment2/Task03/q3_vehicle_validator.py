"""Q3: Normalise, validate and format vehicle registration strings. No regular expressions."""

def normalise(text):
    """Convert e.g. 'tn 09 ab 1234' to 'TN09AB1234'."""
    cleaned = text.strip().replace(" ", "").replace("-", "")
    return cleaned.upper()

def is_valid(reg):
    """Valid: 2 letters, 2 digits, 1-2 letters, 4 digits."""
    if len(reg) not in (9, 10):
        return False
    return (
        reg[0:2].isalpha()
        and reg[2:4].isdigit()
        and reg[4:-4].isalpha()
        and len(reg[4:-4]) in (1, 2)
        and reg[-4:].isdigit()
    )

def format_registration(reg):
    """Format a validated value as 'TN 09 AB 1234'."""
    if not is_valid(reg):
        raise ValueError("Cannot format an invalid registration number")
    return f"{reg[:2]} {reg[2:4]} {reg[4:-4]} {reg[-4:]}"

def main():
    examples = [
        "tn 09 ab 1234",
        "KA-01-M-0007",
        "TN9AB1234",
        "TN 22 1234 AB",
    ]
    for raw in examples:
        reg = normalise(raw)
        status = "valid" if is_valid(reg) else "INVALID"
        formatted = format_registration(reg) if is_valid(reg) else "-"
        print(f"{raw:15} -> {reg:11} {status:7} formatted: {formatted}")
    print("\nSlice examples for TN09AB1234:")
    sample = "TN09AB1234"
    print("s[-4:] =", sample[-4:])
    print("s[4:-4] =", sample[4:-4])

if __name__ == "__main__":
    main()
