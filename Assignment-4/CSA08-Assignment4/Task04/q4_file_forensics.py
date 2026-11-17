"""Task 4: Demonstrate file-mode, newline and error-log defects and repair."""
from pathlib import Path
import tempfile

def bad_save_returns(books, log_path):
    log = open(log_path, "w", encoding="utf-8")
    for book in books:
        log.write(book)
    log.close()

def bad_process(day_file, log_path):
    try:
        books = open(day_file, encoding="utf-8").read().split("\n")
        bad_save_returns(books, log_path)
    except FileNotFoundError:
        print("missing")

def repaired_process(day_file, log_path, error_path):
    try:
        with open(day_file, "r", encoding="utf-8") as source:
            books = [line.strip() for line in source if line.strip()]
        with open(log_path, "a", encoding="utf-8") as log:
            for book in books:
                log.write(book + "\n")
    except FileNotFoundError as exc:
        with open(error_path, "a", encoding="utf-8") as errors:
            errors.write(f"{day_file}: FileNotFoundError: {exc}\n")
    except PermissionError as exc:
        with open(error_path, "a", encoding="utf-8") as errors:
            errors.write(f"{day_file}: PermissionError: {exc}\n")
    except OSError as exc:
        with open(error_path, "a", encoding="utf-8") as errors:
            errors.write(f"{day_file}: OSError: {exc}\n")

def main():
    with tempfile.TemporaryDirectory() as folder:
        base = Path(folder)
        days = []
        for day, books in enumerate((["Book A", "Book B"], ["Book C"], ["Book D", "Book E"]), 1):
            path = base / f"day{day}.txt"
            path.write_text("\n".join(books) + "\n", encoding="utf-8")
            days.append(path)

        bad_log = base / "bad_returns.log"
        for path in days:
            bad_process(path, bad_log)
        print("Bad log (overwritten and joined):")
        print(repr(bad_log.read_text(encoding="utf-8")))

        good_log = base / "returns.log"
        error_log = base / "errors.log"
        for path in days:
            repaired_process(path, good_log, error_log)
        print("Repaired log:")
        print(good_log.read_text(encoding="utf-8"))

        repaired_process(base / "missing.txt", good_log, error_log)
        print("Error log:")
        print(error_log.read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
