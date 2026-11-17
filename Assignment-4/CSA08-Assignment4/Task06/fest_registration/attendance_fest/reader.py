from pathlib import Path

def iter_department_files(folder):
    return sorted(Path(folder).glob("*.txt"))

def iter_lines(path):
    with open(path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            yield line_number, line.rstrip("\n")
