"""Task 3: Custom exceptions and complete try/except/else/finally."""
import os
import tempfile

class InvalidRecord(Exception):
    """Raised when an attendance row is not in the required format."""

def parse_line(line):
    parts = line.strip().split(",")
    if len(parts) != 3:
        raise InvalidRecord(f"expected 3 fields, found {len(parts)}")
    register, date, status = (part.strip() for part in parts)
    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")
    if not register or not date:
        raise InvalidRecord("register number and date must not be empty")
    return register, date, status

def summarise(path):
    present, absent, errors = 0, 0, []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    _, _, status = parse_line(line)
                except InvalidRecord as exc:
                    errors.append((line_number, str(exc)))
                    continue
                if status == "P":
                    present += 1
                else:
                    absent += 1
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"attendance file not found: {path}") from exc
    except PermissionError as exc:
        raise PermissionError(f"permission denied: {path}") from exc
    except UnicodeDecodeError as exc:
        raise ValueError(f"file is not valid UTF-8: {path}") from exc
    else:
        # The file was opened and processed without a file-level exception.
        pass
    finally:
        # with statement closes the file even if processing raises an exception.
        pass
    return present, absent, errors

def main():
    data = (
        "192311001,2026-10-08,P\n"
        "192311002,2026-10-08,A\n"
        "192311003,2026-10-08\n"
        "192311004,2026-10-08,L\n"
    )
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False, encoding="utf-8") as tmp:
        tmp.write(data)
        path = tmp.name
    try:
        print(summarise(path))
    finally:
        os.remove(path)

    try:
        summarise("file_that_does_not_exist.csv")
    except FileNotFoundError as exc:
        print(type(exc).__name__, exc)

if __name__ == "__main__":
    main()
