"""Task 1.2: Safer hostel mess-bill processor."""
from decimal import Decimal, InvalidOperation
from pathlib import Path

def process_mess_file(filename):
    total = Decimal("0.00")
    report_rows = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, raw_line in enumerate(file, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                parts = [part.strip() for part in line.split(",")]
                if len(parts) != 3:
                    rejected.append((line_number, raw_line.rstrip("\n"), "expected 3 fields"))
                    continue
                register, name, amount_text = parts
                try:
                    amount = Decimal(amount_text)
                    if not amount.is_finite():
                        raise InvalidOperation
                except InvalidOperation:
                    rejected.append((line_number, raw_line.rstrip("\n"), "invalid amount"))
                    continue
                report_rows.append(f"{name} {amount:.2f}")
                total += amount
    except FileNotFoundError:
        raise
    except PermissionError:
        raise

    return "\n".join(report_rows), total, rejected

def main():
    filename = Path("mess_oct.txt")
    if not filename.exists():
        filename.write_text(
            "192311001,Arun,1250.50\n"
            "192311002,Bala,980\n"
            "damaged,line\n"
            "192311003,Chitra,abc\n",
            encoding="utf-8"
        )
    report, total, rejected = process_mess_file(filename)
    print(report)
    print("Total", f"{total:.2f}")
    print("Rejected:", rejected)

if __name__ == "__main__":
    main()
