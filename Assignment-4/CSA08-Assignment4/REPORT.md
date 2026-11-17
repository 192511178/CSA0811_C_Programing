# SIMATS ONLINE PROGRAMMING LAB
# PYTHON PROGRAMMING – ASSIGNMENT 4
## CO4: FILE HANDLING, MODULES AND PACKAGES

**Nature:** Individual Assignment  
**Duration:** One Week  
**Total Marks:** 50  
**Bloom's Levels:** K3 – Apply, K4 – Analyse, K5 – Evaluate

## STUDENT DETAILS
Name: ______________________________  
Register Number: ____________________  
Department: _________________________  
Year / Semester: ____________________  
Submission Date: ____________________  
GitHub Repository Link: ______________

---

# ABSTRACT
This assignment focuses on designing and implementing reliable Python programs that process real data files. It covers file handling, reading and writing text files, file modes, encodings, exception handling, custom exceptions, error logging, modules and packages. Six tasks use practical scenarios including hostel mess bills, biometric attendance, library returns, attendance utility organisation and college fest registration. The work emphasises reliable processing of missing, damaged or unexpectedly large data files. Each task includes requirement interpretation, design decisions, pseudocode or implementation, failure analysis, complexity analysis and validation. The final design challenge combines modular programming, input validation, duplicate detection and multiple output reports.

# TABLE OF CONTENTS
1. Introduction and Objectives
2. Software Requirements
3. Task 1 – File-Processing Design Review
4. Task 2 – Biometric Attendance File Design
5. Task 3 – Exception Handling in Attendance Processor
6. Task 4 – File and Exception Forensics
7. Task 5 – Same Utility Organised Four Ways
8. Task 6 – College Fest Registration Desk
9. Overall Complexity and Learning Outcomes
10. GitHub Submission
11. Conclusion
12. Appendix – Execution Evidence

# 1. INTRODUCTION
File handling allows programs to store, retrieve and process information beyond the lifetime of a running program. Real-world files may be missing, empty, malformed, incorrectly encoded, inaccessible or larger than expected. A reliable program must handle these conditions without losing valid data or hiding important errors.

Python provides file modes, context managers, exceptions, modules and packages to organise this work. The `with` statement closes files automatically. Specific exception handlers make failures understandable. Modules and packages separate responsibilities and improve reuse and testing.

## 1.1 Objectives
- Read and write files safely using context managers.
- Process large files line by line.
- Validate records and retain rejected-line details.
- Use appropriate file modes and encodings.
- Identify built-in exceptions and define custom exceptions.
- Apply try, except, else, finally and exception chaining.
- Diagnose append, overwrite and newline defects.
- Organise code as scripts, modules and packages.
- Design a robust multi-file registration processor.
- Compare algorithms using time and space complexity.

# 2. SOFTWARE REQUIREMENTS
| Component | Specification |
|---|---|
| Language | Python 3 |
| IDE | Visual Studio Code or equivalent |
| OS | Windows 11 or compatible |
| Version control | Git and GitHub |
| Encoding | UTF-8 |
| Libraries | Python standard library |
| Main modules | pathlib, os, csv, tempfile, decimal |

Record the exact Python version used for execution in the submitted report.

# 3. TASK 1 – FILE-PROCESSING DESIGN REVIEW: DIAGNOSE AND REPAIR A POOR SCRIPT
**Marks: 6 | K4 – Analyse**

## 3.1 Problem Statement
A hostel office uses a script to total mess bills from a text file containing one line per student: register number, name and amount. The original program hard-codes a file path, reads the entire file, does not close the file explicitly, uses a bare except with pass and builds the report through repeated string concatenation.

## 3.2 Task 1.1 – Diagnose the Script
The following deficiencies can cause operational problems:

| Deficiency | Possible consequence |
|---|---|
| Hard-coded absolute path | Program fails on another computer or after folder changes |
| File not closed | Operating-system resources remain occupied; buffered data may not be flushed |
| `read()` loads whole file | Memory usage grows with file size |
| Bare `except: pass` | Hides damaged records and programming bugs |
| `int()` for amount | Rejects valid paise values such as 1250.50 |
| Repeated `report = report + ...` | Repeated string allocation may waste time |
| Empty final line | May be treated as a malformed record |
| No rejected-line log | Office cannot audit excluded student bills |
| No field-count validation | Missing or extra fields may be used incorrectly |

## 3.3 Task 1.2 – Repaired Design
The repaired implementation is in `Task01/q1_2_repaired_mess.py`.

It uses:
- A function that accepts the filename as a parameter.
- `with open(...)` to guarantee closure.
- UTF-8 encoding.
- Line-by-line iteration.
- `Decimal` for currency amounts.
- Specific validation and exception handling.
- A list of rejected records containing line number, original text and reason.
- A list of report rows combined with `"\n".join(...)`.

## 3.4 Algorithm
1. Receive the input filename.
2. Initialise total to Decimal zero, report rows and rejected rows.
3. Open the file using a context manager.
4. Read each line with its line number.
5. Skip blank lines.
6. Split the line into comma-separated fields.
7. If field count is not three, record the rejected line and continue.
8. Parse the amount using Decimal.
9. If the amount is invalid, record the rejected line and continue.
10. Add valid amount to total and append formatted report row.
11. Return report, total and rejected records.

## 3.5 Task 1.3 – Design Defence (under 100 words)
The repaired program is safer for 50,000 lines because it processes one line at a time instead of loading the entire file into memory. The `with` statement closes the file even if an error occurs. Specific validation prevents malformed records from silently disappearing. Decimal preserves currency precision for paise values. Rejected records are retained with line numbers and reasons, allowing the hostel office to investigate incorrect bills. Passing the filename as a parameter also makes the program reusable across months and computers.

## 3.6 Alternative: read() or readlines()
Both line-by-line iteration and whole-file reading take O(n) time for n characters or bytes processed. However, `read()` and `readlines()` allocate memory proportional to the whole file, O(file size). Iterating line by line requires approximately O(maximum line length) input-buffer space, apart from stored report and rejected records. For 50,000 lines, line-by-line reading is safer when the file is large.

## 3.7 Result
The repaired program calculates valid bill totals, preserves paise precision and records rejected lines for audit.

**Actual output screenshot:** [Insert screenshot.]  
**Rejected-line evidence:** [Insert actual rejected records.]

# 4. TASK 2 – FROM REQUIREMENT TO FILE-PROCESSING DESIGN: BIOMETRIC ATTENDANCE FILES
**Marks: 8 | K3 – Apply**

## 4.1 Problem Statement
Each classroom biometric device creates a daily text file. Each line contains register number, date and P or A. Some records may be damaged. The department requires monthly attendance percentages, a list of students below 75%, and an error log containing filename and line number.

## 4.2 Task 2.1 – Data Model
Input format:
`register_number,date,status`

Example:
`192311001,2026-10-08,P`

The status must be P for present or A for absent.

A dictionary keyed by register number stores present and absent counts. An optional set of processed dates can prevent duplicate records for the same student and day.

Three outputs are appropriate:
1. `attendance_summary.csv`: register number, present, absent, working days and percentage.
2. `below_75.csv`: students whose percentage is below 75.
3. `attendance_errors.csv`: filename, line number, original line and reason.

## 4.3 Task 2.2 – File Operations
- `r`: read daily input files.
- `w`: create fresh monthly summary and error reports.
- `a`: append to a persistent log only when retaining previous runs is intentional.
- UTF-8: explicit encoding for predictable text decoding.
- Iteration: process one line at a time.
- `write()` or `csv.writer`: write output records.
- `readline()`: suitable when one line is specifically required, but iteration is clearer for all records.
- `read()`: not preferred for large daily files because it loads the entire file.

## 4.4 Task 2.3 – Pseudocode
START
  SET attendance dictionary to empty
  SET errors list to empty
  LIST all daily files in the month folder using pathlib
  FOR EACH file in sorted daily files
    TRY
      OPEN file in read mode using UTF-8
      SET line_number to zero
      FOR EACH line in file
        INCREMENT line_number
        IF line is blank THEN CONTINUE
        SPLIT line by comma
        IF field count is not three THEN
          RECORD filename, line number, original line and reason
          CONTINUE
        END IF
        EXTRACT register number, date and status
        IF status is neither P nor A THEN
          RECORD damaged line
          CONTINUE
        END IF
        CREATE student count entry if not present
        INCREMENT present or absent count
      END FOR
    CATCH missing file
      RECORD file failure
    CATCH permission failure
      RECORD access failure
    END TRY
  END FOR
  OPEN summary and below-75 reports for writing
  FOR EACH student in attendance
    CALCULATE working days
    CALCULATE percentage
    WRITE summary row
    IF percentage < 75 THEN WRITE below-75 row
  END FOR
  WRITE error records to error log
STOP

## 4.5 Task 2.4 – Trace
Input:
- Line 1: `192311001,2026-10-08,P`
- Line 2: `192311002,2026-10-08,A`
- Line 3: `192311003,2026-10-08`

Trace:
- Line 1 has three fields and status P; present count for 192311001 becomes 1.
- Line 2 has three fields and status A; absent count for 192311002 becomes 1.
- Line 3 has only two fields; it is added to the error log with its filename and line number. No attendance count changes.

## 4.6 Alternative: Re-read Files for Every Student
If each of s students re-reads f files containing l lines each, the time complexity is O(s·f·l). Reading every file once and accumulating counts in a dictionary takes O(f·l) average processing time. The single-pass method uses O(s + e) memory for student counts and retained errors. Re-reading can reduce the amount of accumulated student state if processing one student at a time, but causes much more file I/O.

## 4.7 Result
The design provides a reliable monthly attendance workflow with separate summary, below-threshold and damaged-record reports.

**Trace screenshot/table:** [Insert evidence.]

# 5. TASK 3 – DESIGN THE ERROR HANDLING: EXCEPTIONS IN THE ATTENDANCE PROCESSOR
**Marks: 9 | K4 – Analyse**

## 5.1 Task 3.1 – Failure Analysis
| Failure | Likely exception | Handling |
|---|---|---|
| Missing folder/file | FileNotFoundError | Report missing path |
| Permission denied | PermissionError | Record access failure |
| Wrong text encoding | UnicodeDecodeError | Record invalid encoding |
| Damaged field count/status | Custom InvalidRecord or ValueError | Log line and continue |
| Missing field access | IndexError | Validate field count before indexing |
| Invalid numeric conversion | ValueError | Record invalid value |
| Empty file | No exception by itself | Return zero counts |
| Path points to directory | IsADirectoryError | Record invalid input path |
| Other operating-system I/O failure | OSError | Record operational failure |

## 5.2 Task 3.2 – Custom Exception
`InvalidRecord` is defined as a subclass of Exception. It is raised inside `parse_line()` when the line does not contain exactly three fields or when the status is not P or A. It is handled inside the per-line processing loop so one damaged record does not stop the entire file.

## 5.3 Task 3.3 – Complete try Statement
The implementation in `Task03/q3_exceptions_attendance.py` demonstrates:
- `try`: opens and processes the file.
- `except`: handles InvalidRecord per line and file-level exceptions separately.
- `else`: runs when the file-level try block completes without exception.
- `finally`: provides a cleanup location; the `with` statement already guarantees closure.
- `raise ... from ...`: preserves the original exception as the cause when adding context to FileNotFoundError, PermissionError or decoding errors.

## 5.4 Task 3.4 – Misuse Experiment
Replacing specific handlers with `except Exception: pass` hides errors. For example, if `present_count` is accidentally typed as `presnt_count`, Python raises NameError. A broad handler that silently passes suppresses the NameError, so the program appears to continue while the attendance total is wrong or incomplete. This makes debugging and auditing difficult.

## 5.5 Expected Output for Complete Code
`(1, 1, [(3, 'expected 3 fields, found 2'), (4, "invalid status 'L'")])`

The program also attempts to open a non-existent file and demonstrates handling FileNotFoundError.

## 5.6 Alternative: EAFP and LBYL
EAFP means “Easier to Ask Forgiveness than Permission”: attempt the operation and catch a specific exception if it fails. LBYL means “Look Before You Leap”: check conditions before performing the operation.

When bad lines are rare, EAFP can be concise and successful lines avoid multiple pre-checks, though exception creation and handling has overhead. When bad lines are common, LBYL validation can be more efficient because it detects expected invalid data using ordinary conditions rather than repeatedly raising exceptions. Both approaches are O(1) work per line for fixed validation rules, so processing n lines is O(n); actual constants differ.

## 5.7 Result
Custom exceptions distinguish invalid data from file-system failures and allow the processor to continue after a damaged row while preserving useful diagnostic information.

**Execution output:** [Insert screenshot.]

# 6. TASK 4 – FILE AND EXCEPTION FORENSICS
**Marks: 7 | K4 – Analyse**

## 6.1 Task 4.1 – Locate the Defects
The original library program opens `returns.log` in write mode (`w`). Each daily run truncates the existing file, so earlier days are lost. It writes each book name without a newline, so entries are joined together. If `write()` raises an exception before `close()`, the file may remain open until cleanup occurs, and buffered data may not be flushed reliably.

The source input file is also opened without a context manager and is not explicitly closed.

## 6.2 Task 4.2 – Construct Evidence
A test creates three daily files and runs the defective program for each. The final log contains only the third day's entries because each run overwrites the file. The absence of newline characters makes multiple book names appear as one continuous string.

The implementation in `Task04/q4_file_forensics.py` demonstrates the defective output and corrected output.

## 6.3 Task 4.3 – Repair
The repaired implementation:
- Opens source files using `with`.
- Opens the log in append mode (`a`).
- Writes `book + "\n"` for each book.
- Handles FileNotFoundError and PermissionError.
- Writes diagnostic details to a separate error log.

## 6.4 Task 4.4 – Prevention Rules
1. Use `with open(...)` for every file so resources are closed even when exceptions occur.
2. Choose file mode deliberately: use `w` for a fresh report and `a` for a persistent log; include explicit newline separators.

## 6.5 Alternative: Manual try/finally
The equivalent manual pattern opens the file, performs writes inside `try`, and closes it in `finally`. For example, initialise the file variable, open it, write records, and close it in the finally block if opening succeeded. This has the same O(n) time and O(1) additional space for streaming writes as the context-manager version. Both should leave zero files open after normal cleanup; `with` expresses the guarantee more clearly and is less error-prone.

## 6.6 Result
The repaired program preserves all three days of returns, separates entries with newlines and records file errors for later investigation.

**Before/after log screenshot:** [Insert screenshot.]

# 7. TASK 5 – THE SAME UTILITY ORGANISED FOUR WAYS
**Marks: 7 | K5 – Evaluate**

## 7.1 Problem Statement
The attendance processor has three groups of functions: reading files, computing statistics and writing reports. It must be organised as one script, one imported module, three modules in a folder and a package with `__init__.py`, `reader.py`, `stats.py` and `report.py`.

## 7.2 Four Organisations
(a) One script: all reading, statistics and report-writing functions are in one Python file.

(b) One module plus main script: reusable functions are placed in `attendance_utils.py` and imported by `main.py`.

(c) Three modules: `reader.py`, `stats.py` and `report.py` separate responsibilities, while `main.py` coordinates them.

(d) Package: `attendance/` contains `__init__.py`, `reader.py`, `stats.py` and `report.py`. The package version is implemented under `Task05/d_package/`.

## 7.3 Main Guard
`if __name__ == "__main__":` ensures that demonstration or command-line code runs only when a module is executed directly, not when imported by another module.

## 7.4 Task 5.2 – Requirement Change
The new requirement is to generate a second report listing students absent for three consecutive days.

A clean design adds the consecutive-absence calculation to the statistics responsibility and adds another output function/report call.

Expected change effort:
- One script: edit the same file; logic and I/O are mixed.
- One module: update the utility module and main script if a new output is required.
- Three modules: update stats.py and report.py, and possibly main.py to connect the new result.
- Package: update stats.py and report.py, and update the package interface only if the new function is exported from `__init__.py`.

The exact number of changed files depends on the chosen public API and should be recorded from the student's implementation.

## 7.5 Task 5.3 – Comparison
| Organisation | Readability | Reuse | Testing | Naming conflicts |
|---|---|---|---|---|
| One script | Declines as file grows | Low | Harder to isolate | Low within one namespace |
| One module | Better separation from main | Moderate | Functions can be tested | Possible generic module names |
| Three modules | Clear responsibility boundaries | High | Easier unit testing | Manageable with careful imports |
| Package | Strong organisation and public API | Highest for larger projects | Modules test independently | Package namespace reduces conflicts |

Import forms:
- `import attendance.stats`: imports the submodule; access with `attendance.stats.percentage` after the package is available.
- `from attendance import stats`: imports the stats submodule through the package namespace.
- `from attendance.stats import percentage`: imports the function directly into the current namespace.

## 7.6 Alternative: One Script Instead of Package
A single script avoids package organisation and has no separate package import cost, but locating, testing and changing a function becomes harder as the file grows. A package has a one-time import and module initialisation cost; imported modules are cached in `sys.modules`, so repeated imports generally reuse the loaded module. Package code and module objects occupy memory while loaded. The asymptotic runtime of the attendance calculations does not change merely because functions are split into modules.

## 7.7 Result
The package organisation is most suitable when the attendance utility is expected to grow and be reused. It separates file reading, calculations and report generation and supports independent testing.

**Evidence:** [Insert screenshots or folder trees for all four layouts.]

# 8. TASK 6 – DESIGN CHALLENGE: COLLEGE FEST REGISTRATION DESK
**Marks: 13 | K5 – Evaluate**

## 8.1 Problem Statement
Registrations arrive as text files from five departments. Each line contains register number, name, department, email and semicolon-separated events. Some students register twice, email addresses may be invalid and some lines may be damaged. The committee needs a clean master list, event-wise participant files, a summary report and an error log. The program must continue despite bad lines or missing files.

## 8.2 Stage 1 – Inputs, Outputs and Testable Rules
Inputs:
- Department registration text files.
- One record per line with five comma-separated fields.
- Events separated by semicolons.

Outputs:
- `master_list.csv`
- One `event_<name>.csv` per event.
- `summary.txt`
- `error_log.csv`

Testable rules:
1. A valid line contains exactly five fields.
2. Register number, name and department are non-empty.
3. Email contains exactly one `@`, a non-empty local part and a domain containing a dot.
4. At least one event must be selected.
5. A register number is accepted only once; later duplicates are logged.
6. Every invalid line is logged with source filename and line number.
7. A missing expected department file is logged.
8. A bad line must not terminate processing of later records.
9. Output files use UTF-8 and are closed reliably.

## 8.3 Stage 2 – Processing Flow
Department files → line-by-line reader → record parser and validation → duplicate check using seen-register set/dictionary → master dictionary and event grouping → master list, event files and summary. Invalid records, duplicates, missing files and file errors → error log.

## 8.4 Stage 3 – Critical Decisions
Duplicate detection: maintain a dictionary keyed by register number. Average membership and insertion are O(1). Keep the first valid registration and log later duplicates.

Email validation: use string methods such as `count("@")`, `split("@")`, checks for a non-empty local part and a dot in the domain. This is a basic validation rule, not a complete email-standard validator.

Exception handling:
- InvalidRegistration: raised for damaged fields and invalid data; caught per line.
- FileNotFoundError: caught per input file or recorded when an expected file is missing.
- PermissionError: caught per file.
- UnicodeDecodeError: caught for invalid UTF-8 input.
- OSError: catches other file-system failures.

## 8.5 Stage 4 – Package Structure
`attendance_fest/`
- `__init__.py`: package interface.
- `reader.py`: lists input files and yields numbered lines.
- `validator.py`: custom exception and record validation.
- `processor.py`: duplicate handling, grouping, output generation and error logging.
- `run_fest.py`: demonstration entry point.

The working implementation is provided in `Task06/fest_registration/`.

## 8.6 Pseudocode
START
  CREATE output directory if it does not exist
  CREATE empty master dictionary
  CREATE empty event-to-participants dictionary
  CREATE empty error list
  LIST department files
  CHECK expected department files and log missing ones
  FOR EACH department file
    TRY
      OPEN file as UTF-8
      FOR EACH numbered line
        IF line is blank THEN CONTINUE
        TRY
          VALIDATE exactly five fields
          VALIDATE required fields and email
          SPLIT selected events
          IF register number already exists THEN
            LOG duplicate
            CONTINUE
          END IF
          STORE registration in master dictionary
          ADD registration to each selected event group
        CATCH InvalidRegistration
          LOG filename, line number, original line and reason
        END TRY
      END FOR
    CATCH file-related exception
      LOG file failure
    END TRY
  END FOR
  WRITE master list CSV
  FOR EACH event group
    WRITE event participant CSV
  END FOR
  WRITE summary report
  WRITE error log
STOP

## 8.7 Stage 5 – Implementation and Demonstration
The sample implementation demonstrates:
- Clean registrations.
- A duplicate register number.
- An invalid email address.
- A damaged line with the wrong field count.
- A missing expected department file.
- Event-wise participant output.
- Master list, summary and error log generation.

Run from `Task06/fest_registration/`:
`python run_fest.py`

Expected evidence should include the generated files in the output folder and the terminal summary.

## 8.8 Alternative: Search a List of Earlier Registrations
A list-based design can compare each new register number with every previously accepted registration. In the worst case, the first, second and subsequent records perform an increasing number of comparisons, producing O(n²) total time for n registrations. A set or dictionary of previously seen register numbers provides O(1) average membership checks, making total duplicate detection O(n) average. Both approaches require O(n) space to retain accepted registrations; the set/dictionary adds indexing overhead.

## 8.9 Result
The college fest registration package processes multiple department files, validates records, avoids duplicate registrations, groups participants by event and writes a master list, summary and error log. File-level and record-level failures are recorded so processing can continue.

**Execution screenshots:** [Insert terminal and generated-file screenshots.]  
**Test cases:** [Record actual outcomes for clean, duplicate, invalid email, damaged line and missing file.]

# 9. OVERALL COMPLEXITY AND LEARNING OUTCOMES

| Task | Main concept | Key efficiency point |
|---|---|---|
| 1 | File iteration and Decimal | O(n) processing with line-sized input memory |
| 2 | Dictionary accumulation | O(f·l) versus O(s·f·l) repeated scans |
| 3 | Specific exceptions | Per-line validation and controlled recovery |
| 4 | Append mode and context managers | Streaming O(n) writing |
| 5 | Modules and packages | Better reuse and testability; import initialisation cost |
| 6 | Set/dictionary duplicate detection | O(n) average versus O(n²) list search |

Learning outcomes:
1. Use context managers to manage file resources.
2. Read large files line by line.
3. Validate file records and preserve rejected data.
4. Select suitable file modes and encodings.
5. Identify and handle built-in exceptions.
6. Define and use custom exceptions.
7. Use exception chaining to preserve original causes.
8. Diagnose file overwrite and newline defects.
9. Organise programs into modules and packages.
10. Build a robust multi-file processing system.
11. Compare algorithmic approaches using Big-O notation.

# 10. GITHUB SUBMISSION

Repository name:

`CSA08-RegisterNumber-Assignment4`

Required structure:
- `Task01/` – repaired mess-bill processor and sample data.
- `Task02/` – attendance data model, pseudocode and trace.
- `Task03/` – custom exception attendance processor.
- `Task04/` – file forensics demonstration.
- `Task05/` – all four organisation approaches.
- `Task06/` – fest registration package and sample input/output.
- `README.md`
- `requirements.txt`
- `REPORT.md`

At least one progressive commit is required for each task. Suggested commit messages:
1. Add Task01 – Repair mess bill processor.
2. Add Task02 – Attendance file processing design.
3. Add Task03 – Custom exception handling.
4. Add Task04 – File handling forensics.
5. Add Task05 – Module and package comparison.
6. Add Task06 – College fest registration package.
7. Add final report and execution evidence.

The repository must be public or shared with the course faculty as a collaborator if private.

# 11. CONCLUSION

This assignment developed practical understanding of reliable file processing, exception handling, modules and packages in Python.

Task 1 demonstrated how to diagnose and repair a poor file-processing script. Task 2 designed a monthly biometric attendance workflow using dictionary accumulation and line-by-line reading. Task 3 applied specific and custom exceptions to handle damaged attendance records. Task 4 investigated overwrite, newline and file-closing defects and repaired them using append mode and context managers. Task 5 compared four ways of organising the same utility and evaluated modularity and reuse. Task 6 combined these concepts in a college fest registration package that validates data, detects duplicates, groups event participants and produces reports.

The assignment emphasises that reliable software must not only produce correct results for clean input but must also handle missing, malformed and inaccessible files without silently losing information.

# 12. APPENDIX – EXECUTION EVIDENCE

Task 1:
- Original design diagnosis.
- Repaired program output.
- Rejected line list and currency total.

Task 2:
- Attendance input example.
- Data model and trace.
- Pseudocode and report design.

Task 3:
- Custom exception code.
- Expected output.
- Missing-file handling.
- Misuse experiment output.

Task 4:
- Defective log output from three days.
- Repaired append-mode output.
- Error log.

Task 5:
- Folder structures for all four organisations.
- Import examples and main-guard output.
- Record of files changed for the new consecutive-absence requirement.

Task 6:
- Sample department input files.
- Master list.
- Event-wise participant files.
- Summary report.
- Error log.
- Screenshots of duplicate, invalid email, damaged line and missing-file cases.

---

**GitHub Repository Link:** ______________________________

**Student Name:** ______________________________________

**Register Number:** ____________________________________

**Submission Date:** ____________________________________

# END OF REPORT
