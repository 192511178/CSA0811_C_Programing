import csv
from pathlib import Path
from .reader import iter_department_files, iter_lines
from .validator import parse_registration, InvalidRegistration

def process_department_files(input_folder, output_folder, expected_files=None):
    output = Path(output_folder)
    output.mkdir(parents=True, exist_ok=True)
    master = {}
    event_participants = {}
    errors = []

    files = iter_department_files(input_folder)
    found_names = {p.name for p in files}
    if expected_files:
        for expected in expected_files:
            if expected not in found_names:
                errors.append((expected, 0, "", "missing department file"))

    for path in files:
        try:
            for line_number, line in iter_lines(path):
                if not line.strip():
                    continue
                try:
                    record = parse_registration(line)
                    reg = record["register_number"]
                    if reg in master:
                        # First valid registration is retained; duplicate is logged.
                        errors.append((path.name, line_number, line, f"duplicate register number {reg}"))
                        continue
                    master[reg] = record
                    for event in record["events"]:
                        event_participants.setdefault(event, []).append(record)
                except InvalidRegistration as exc:
                    errors.append((path.name, line_number, line, str(exc)))
        except FileNotFoundError as exc:
            errors.append((path.name, 0, "", f"missing file: {exc}"))
        except PermissionError as exc:
            errors.append((path.name, 0, "", f"permission denied: {exc}"))
        except UnicodeDecodeError as exc:
            errors.append((path.name, 0, "", f"invalid UTF-8: {exc}"))
        except OSError as exc:
            errors.append((path.name, 0, "", f"file error: {exc}"))

    # Master list
    with open(output / "master_list.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["register_number", "name", "department", "email", "events"])
        for record in master.values():
            writer.writerow([record["register_number"], record["name"], record["department"],
                             record["email"], ";".join(record["events"])])

    # One participant file per event
    for event, records in event_participants.items():
        safe_event = "".join(ch for ch in event if ch.isalnum() or ch in ("-", "_")) or "event"
        with open(output / f"event_{safe_event}.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["register_number", "name", "department", "email"])
            for record in records:
                writer.writerow([record["register_number"], record["name"],
                                 record["department"], record["email"]])

    with open(output / "summary.txt", "w", encoding="utf-8") as f:
        f.write(f"Total unique registrations: {len(master)}\n")
        f.write(f"Total events: {len(event_participants)}\n")
        for event, records in sorted(event_participants.items()):
            f.write(f"{event}: {len(records)} participants\n")

    with open(output / "error_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["filename", "line_number", "original_line", "reason"])
        writer.writerows(errors)

    return master, event_participants, errors
