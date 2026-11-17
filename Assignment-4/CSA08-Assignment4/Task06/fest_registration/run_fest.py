from pathlib import Path
from attendance_fest.processor import process_department_files

def create_demo_inputs(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "department_cse.txt").write_text(
        "192311001,Anu,CSE,anu@example.com,Music;Dance\n"
        "192311002,Bala,CSE,bala@example.com,Drama\n"
        "192311001,Anu,CSE,anu@example.com,Music\n"
        "192311003,Charu,CSE,invalid-email,Quiz\n"
        "damaged,line\n", encoding="utf-8")
    (folder / "department_ece.txt").write_text(
        "192311004,Deepa,ECE,deepa@example.com,Music;Quiz\n", encoding="utf-8")

if __name__ == "__main__":
    base = Path(__file__).parent
    inputs, outputs = base / "sample_input", base / "output"
    create_demo_inputs(inputs)
    master, events, errors = process_department_files(
        inputs, outputs, expected_files=["department_cse.txt", "department_ece.txt", "department_mech.txt"]
    )
    print("Unique registrations:", len(master))
    print("Events:", sorted(events))
    print("Errors logged:", len(errors))
    print("Output folder:", outputs)
