# Task 2 – Biometric Attendance File Processing Design

## Data model
Input: one UTF-8 text/CSV file per day. Each non-empty line has exactly three comma-separated fields:
`register_number,date,status`, where status is `P` or `A`.

Accumulator: dictionary keyed by register number. Each value stores `present`, `absent`, and optionally a set of dates already processed to prevent duplicate day records.

Output 1: `attendance_summary.csv` with register number, present count, working-day count and percentage.
Output 2: `below_75.csv` containing students whose percentage is below 75%.
Damaged-record log: `attendance_errors.csv` with source filename, line number, original line and error reason.

## File operations
- Use `pathlib.Path.glob("*.txt")` or `os.listdir()` to locate daily files.
- Open input files in `r` mode with `encoding="utf-8"`.
- Iterate line by line rather than loading all files into memory.
- Open reports in `w` mode once, and use `csv.writer` or `write()` to emit rows.
- Open the error log in `w` mode for a fresh monthly run; use `a` only when deliberately appending to an existing log.
- Use `with` so files close reliably.

## Pseudocode (SIMATS-style)
START
  SET attendance = empty dictionary
  SET errors = empty list
  FOR EACH file_path IN sorted(month_folder.glob("*.txt"))
    TRY
      OPEN file_path FOR reading as UTF-8
      SET line_number = 0
      FOR EACH line IN file
        INCREMENT line_number
        IF line is blank THEN CONTINUE
        SPLIT line by comma into fields
        IF field count is not 3 THEN
          ADD (file_path, line_number, line, "wrong field count") TO errors
          CONTINUE
        END IF
        EXTRACT register_number, date, status
        IF status is not P or A THEN
          ADD damaged record to errors
          CONTINUE
        END IF
        IF register_number is not in attendance THEN
          CREATE present=0, absent=0 for register_number
        END IF
        IF status is P THEN INCREMENT present
        ELSE INCREMENT absent
        END IF
      END FOR
    CATCH FileNotFoundError
      ADD missing-file detail TO errors
    CATCH PermissionError
      ADD permission detail TO errors
    END TRY
  END FOR
  OPEN summary report FOR writing
  FOR EACH student IN attendance
    SET working_days = present + absent
    CALCULATE percentage = present / working_days * 100
    WRITE student summary
    IF percentage < 75 THEN WRITE student to below-75 report
  END FOR
  WRITE all errors to error log
STOP

## Trace example
Input:
192311001,2026-10-08,P
192311002,2026-10-08,A
192311003,2026-10-08

Trace:
- Line 1: valid P; student 192311001 present becomes 1.
- Line 2: valid A; student 192311002 absent becomes 1.
- Line 3: only two fields; record is logged with filename and line number; counts unchanged.

## Complexity
Let s = students, f = files, l = average lines per file.
Single-pass accumulation: O(f·l) time and O(s + e) memory, where e is retained error information.
Re-reading every file for each student: O(s·f·l) time. It may use less accumulator memory if each student is processed separately, but requires repeated I/O.
