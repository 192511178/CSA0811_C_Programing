# SIMATS ONLINE PROGRAMMING LAB
# PYTHON PROGRAMMING – ASSIGNMENT 3
## CO3: PYTHON DATA STRUCTURES

**Assignment:** Assignment 3  
**Total Marks:** 50  
**Nature:** Individual  
**Duration:** One Week  

### STUDENT DETAILS
Name: ______________________________  
Register Number: ____________________  
Department: _________________________  
Year / Semester: ____________________  
Submission Date: ____________________  
GitHub Repository Link: ______________

---

# ABSTRACT
This assignment explores Python data structures and their practical applications, focusing on lists, tuples, dictionaries, sets, list comprehensions and nested data structures. Seven real-world problems are used to demonstrate how data can be stored, accessed, modified, analysed and optimised. The tasks include rainfall record processing, bus-stop coordinate storage, farmer helpline complaint analysis, elective registration clash detection, sensor reading cleaning, railway timetable queries and contact merging. Each task requires implementation, testing, analysis and evaluation. Experimental investigations measure execution time and memory where specified. The assignment develops practical understanding of data-structure selection, mutability, copying, lookup efficiency, comprehensions, indexing and algorithmic complexity.

# TABLE OF CONTENTS
1. Introduction and Objectives
2. Software Requirements
3. Q1 – Lists and Slicing: Daily Rainfall Records
4. Q2 – Tuples, Mutability and Copying
5. Q3 – Dictionaries: Farmer Helpline Complaint Analysis
6. Q4 – Sets: Elective Registration Clash Detection
7. Q5 – List Comprehension: Cleaning Sensor Readings
8. Q6 – Nested Data: A Railway Timetable
9. Q7 – Contact-Merging Program from First Principles
10. Overall Analysis and Learning Outcomes
11. GitHub Submission
12. Conclusion
13. Execution Evidence

# 1. INTRODUCTION
Python provides built-in data structures that help store and manipulate collections of information. Lists are ordered and mutable; tuples are ordered and immutable at the outer level; dictionaries store key-value mappings; and sets store unique hashable elements. List comprehensions provide a concise way to construct lists, while nested structures combine data types to model real-world information.

This assignment applies these structures to practical scenarios. Each question follows the design, implementation, analysis and evaluation process required by the assignment brief.

## 1.1 Objectives
- Apply list operations and slicing to rainfall data.
- Understand tuple immutability, aliasing and copying.
- Use dictionaries to count and group complaint data.
- Apply set operations to detect registration clashes.
- Clean and transform sensor data using loops, comprehensions, map and filter.
- Represent railway information using nested dictionaries, lists, tuples and sets.
- Design a contact-merging solution using normalised keys and sets.
- Measure execution time and memory and compare alternative approaches.

# 2. SOFTWARE REQUIREMENTS
| Component | Specification |
|---|---|
| Language | Python 3 |
| IDE | Visual Studio Code or equivalent |
| Operating System | Windows 11 or compatible |
| Version Control | Git and GitHub |
| Libraries | Python standard library |
| Main modules | random, time, csv, copy, sys, collections, re |

Enter the exact Python version used for execution in the final report.

# 3. Q1 – LISTS AND SLICING: DAILY RAINFALL RECORDS
**Marks: 6 | Level: K3 – Apply**

## 3.1 Problem Statement
A village rain-gauge station records rainfall in millimetres every day for a year. The data is stored as a list of 365 values. The panchayat requires weekly totals, the wettest and driest readings or weeks, a seven-day moving average and a list of dry days.

## 3.2 Data Structure Selection
A list is suitable because rainfall readings are ordered by day, can be accessed by index, can be sliced into weekly sections and can be extended when new readings arrive. Lists are mutable, so readings can be updated when corrections are received.

## 3.3 Implementation
The program stores rainfall readings in a list. Weekly totals are calculated by slicing seven readings at a time. Maximum and minimum readings are found with their positions. Dry days are identified by checking for values equal to zero.

A seven-day moving average is calculated in two ways:
- Naive method: calculate `sum(readings[i:i+7]) / 7` for each window.
- Running-sum method: calculate the first window sum once, then add the new reading and subtract the reading leaving the window.

## 3.4 Pseudocode for Running Moving Average
1. If the number of readings is less than seven, return an empty result.
2. Calculate the sum of the first seven readings.
3. Store the first average.
4. For each following day, add the new reading and subtract the oldest reading in the window.
5. Divide the updated sum by seven and append the average.
6. Return all averages.

## 3.5 Slicing Explanation
- `readings[7:14]` returns elements at indices 7 through 13, the second group of seven readings.
- `readings[-7:]` returns the final seven readings.
- `readings[::7]` returns every seventh element, beginning at index zero. It does not calculate weekly totals.

## 3.6 List Operation Costs
- `append()` is O(1) amortised.
- `insert()` at an arbitrary position is O(n), because later elements may need to shift.
- `pop()` at the end is O(1); removing from the middle or beginning is O(n).
- `sort()` is O(n log n) in the general case.

If a late reading must be inserted at its correct date in a list, insertion can cost O(n). A list remains reasonable for a year of daily readings, but frequent out-of-order insertions may motivate a different structure.

## 3.7 Experimental Investigation
The program generates 365, 36,500 and 365,000 random readings. It times the naive and running-sum methods and saves results in `q1_timings.csv`. Empty and shorter-than-seven lists are also tested.

For a window size of seven, the naive method performs up to seven additions for each output position, approximately 7(n−6) additions. The running-sum method uses six initial additions plus approximately two arithmetic updates for each later position, so it is O(n).

## 3.8 Alternative: deque or Dictionary
A `collections.deque(maxlen=7)` is useful for maintaining only the latest seven readings as a stream arrives. It supports efficient append and automatic removal from the opposite end. A dictionary keyed by date supports date-based lookup and correction, though chronological ordering and moving-window traversal require additional handling.

The running-sum approach takes O(n) time for n readings and O(n) output space if all averages are stored. A streaming deque can use O(7), effectively O(1), window space if only the current average is required.

## 3.9 Result
The rainfall task demonstrates list storage, slicing, indexing, extrema, dry-day filtering and moving-average computation. The running-sum method reduces repeated work compared with recalculating every seven-value sum.

**Actual timings and observations:** [Insert values from q1_timings.csv.]  
**Output screenshot:** [Insert screenshot.]

# 4. Q2 – TUPLES, MUTABILITY AND COPYING
**Marks: 7 | Level: K4 – Analyse**

## 4.1 Problem Statement
A city bus service stores each bus stop's GPS coordinate as a latitude-longitude pair and uses a grid to count passengers boarding in each zone. A grid created using `[[0] * cols] * rows` contains references to the same row list. Updating one row therefore appears in every row.

## 4.2 Implementation
Each stop is represented by a tuple, such as `(13.0827, 80.2707)`, and tuples are used as dictionary keys. The zone grid is correctly created using a nested list comprehension so each row is a separate list.

The program demonstrates aliasing, shallow copies using `copy.copy()` and slicing, and deep copies using `copy.deepcopy()`. It also unpacks coordinate tuples in a for loop.

## 4.3 Why Tuples Can Be Dictionary Keys
Dictionary keys must be hashable. A tuple containing hashable values, such as floats, is hashable and can be used as a key. Lists are mutable and unhashable, so attempting to use a list as a dictionary key raises `TypeError`.

A tuple is immutable at its outer level, but a tuple can contain a mutable object such as a list. The contained list can still be modified.

## 4.4 Aliasing and Copying
Aliasing occurs when two variables refer to the same object. A shallow copy creates a new outer container but keeps references to nested objects. A deep copy recursively copies nested objects as well.

A shallow copy is sufficient when nested objects are immutable or are intentionally shared. A deep copy is required when nested mutable objects must be independent.

A function that modifies a list argument changes the caller's list because the function receives a reference to the same list object.

## 4.5 Grid Memory Diagram
Incorrect grid:
- Row 1 → same list object
- Row 2 → same list object
- Row 3 → same list object

Correct grid:
- Row 1 → independent list object
- Row 2 → independent list object
- Row 3 → independent list object

The program verifies this with `is` and `id()`.

## 4.6 Experimental Investigation
The program compares `sys.getsizeof()` for a list and tuple containing one million values, and times indexing operations. The reported size is the shallow container size; it does not include the full memory occupied by all referenced integer objects. Tuple and list creation and indexing can be measured separately for a more complete experiment.

## 4.7 Alternative: Sparse Dictionary Grid
A dictionary keyed by `(row, col)` tuples can store only zones containing passengers. Average dictionary access is O(1). A full list-of-lists grid uses O(rows × cols) space. A sparse dictionary uses O(number of non-empty zones) space, with additional dictionary overhead.

## 4.8 Result
This task demonstrates tuple hashability, list mutability, aliasing, shallow copying, deep copying and safe creation of independent nested lists.

**Actual memory and timing results:** [Insert measurements.]  
**Output screenshot:** [Insert screenshot.]

# 5. Q3 – DICTIONARIES: FARMER HELPLINE COMPLAINT ANALYSIS
**Marks: 7 | Level: K4 – Analyse**

## 5.1 Problem Statement
A farmer helpline records complaint text. The agriculture department needs frequent complaint words while ignoring common stop words, complaint counts by district and complaint lists grouped by crop or district.

## 5.2 Dictionary Frequency Counting
A dictionary stores each word as a key and its frequency as a value. The program converts text to lowercase, extracts words, removes stop words and increments the frequency using `dict.get()`. `setdefault()` is also demonstrated as an alternative.

The top-k words are sorted by descending frequency and then alphabetically. Alphabetical tie-breaking ensures deterministic ordering.

## 5.3 District Grouping
A dictionary maps each district to a list of complaints. `setdefault()` creates an empty list for a district when it is first encountered, after which the complaint is appended.

## 5.4 Dictionary Lookup and Ordering
A dictionary uses hashing to locate a key. Lookup is O(1) on average, although collisions can make individual operations slower. Python dictionaries preserve insertion order as a language guarantee from Python 3.7 onward.

- `keys()` provides a view of keys.
- `values()` provides a view of values.
- `items()` provides a view of key-value pairs.

These are dynamic views reflecting changes to the dictionary.

## 5.5 Dictionary vs list.count()
Counting with a dictionary processes each word and updates its count, giving O(n) average time for n tokens. Calling `list.count()` for every distinct word scans the entire list each time, giving O(n × d) for d distinct words. `collections.Counter` is a specialised counting tool with expected linear processing time.

## 5.6 Experimental Investigation
The program generates 1,000, 10,000 and 100,000 complaints and compares dictionary counting, list.count() and Counter. It also tests empty text, case differences and punctuation. Results are saved in `q3_timings.csv`.

## 5.7 Engineering Decision
For 100,000 complaints per day, a dictionary or `collections.Counter` is preferable to repeated list.count() because it avoids rescanning the full token list for every distinct word. The dictionary approach also supports grouping and custom processing.

## 5.8 Result
The task demonstrates dictionary frequency counting, stop-word filtering, deterministic top-k sorting and grouping complaints by district.

**Expected sample output:** `[('seeds', 3), ('price', 2), ('received', 2)]`. Price comes before received because both have frequency two and alphabetical order is the tie-breaker.

**Actual timings:** [Insert values from q3_timings.csv.]  
**Output screenshot:** [Insert screenshot.]

# 6. Q4 – SETS: ELECTIVE REGISTRATION CLASH DETECTION
**Marks: 7 | Level: K4 – Analyse**

## 6.1 Problem Statement
Students register for electives offered in the same time slot. The academic office needs to identify students registered in both electives, exactly one elective, and neither elective.

## 6.2 Set Operations
Each elective's register numbers are stored in a set. Sets automatically remove duplicates.

- Intersection (`&`) finds students in both electives.
- Symmetric difference (`^`) finds students in exactly one elective.
- Union (`|`) finds students in either elective.
- Difference (`-`) finds students in one set but not the other.

Students in neither elective are calculated by subtracting the union from the complete student set.

## 6.3 Expected Output
- Clash: `192311004`, `192311009`
- Exactly one: `192311001`, `192311002`, `192311007`, `192311010`
- Neither: `192311003`, `192311005`, `192311006`, `192311008`

The program sorts results before printing to make the report predictable.

## 6.4 Set Properties
Sets cannot contain duplicate elements. Membership testing is O(1) on average for a set, while list membership is O(n) because elements may need to be checked sequentially.

Sets require hashable elements. Lists are mutable and unhashable, so they cannot be members of a set. Tuples containing hashable elements can be members.

A Venn diagram can represent the two elective sets: the intersection is the overlap, symmetric difference is the non-overlapping portions, and neither is outside both circles but inside the full student universe.

## 6.5 Experimental Investigation
The program compares list and set membership for 10,000, 100,000 and 1,000,000 register numbers. It also verifies empty and identical elective cases and compares set operations with the expected small example. Results are saved in `q4_membership_timings.csv`.

## 6.6 Alternative: Lists and Sorting
Nested list comparisons can take O(n × m) time for sets of sizes n and m. Sorting both lists and walking through them takes O(n log n + m log m). Set operations take O(n + m) expected time overall, with additional space for result sets.

Converting a list to a set is useful when repeated membership tests or duplicate removal are needed. The conversion loses duplicate counts and original positional order.

## 6.7 Result
The task demonstrates how set operations efficiently identify overlaps, exclusive registrations and students without registrations.

**Actual timings:** [Insert values from q4_membership_timings.csv.]  
**Output screenshot:** [Insert screenshot.]

# 7. Q5 – LIST COMPREHENSION: CLEANING SENSOR READINGS
**Marks: 6 | Level: K3 – Apply**

## 7.1 Problem Statement
A cold-storage unit for vaccines records temperature every minute. Values above 50°C or below −50°C are considered sensor errors. The pharmacist requires valid Celsius readings, converted Fahrenheit readings and the minutes when valid temperature readings fall outside 2–8°C.

## 7.2 Implementation Methods
The program implements three approaches:
1. A for loop with append().
2. List comprehensions with conditions.
3. map() and filter() with lambda functions.

The program also uses enumerate() to identify the positions of alarm readings.

The Fahrenheit conversion formula is:

F = (C × 9/5) + 32

Valid sensor values satisfy −50 ≤ C ≤ 50. An alarm is generated for a valid reading outside the safe range 2–8°C.

## 7.3 List Comprehension
General form:

`[expression for item in iterable if condition]`

A comprehension constructs a list by evaluating an expression for each item that satisfies the condition.

A comprehension can become harder to read when it contains several nested loops, complex conditions or multiple transformations. In those cases, a normal loop may be clearer.

## 7.4 Dictionary and Set Comprehensions
A dictionary comprehension creates key-value pairs, for example mapping each valid reading index to its temperature. A set comprehension creates unique valid temperature values.

## 7.5 List Comprehension vs Generator Expression
A list comprehension creates the complete list in memory. A generator expression produces values lazily as they are requested. A list uses O(n) storage for n results, while a generator generally uses O(1) additional iterator state, excluding the source data.

## 7.6 Experimental Investigation
The program tests 10,000, 100,000 and 1,000,000 readings and measures the three implementation approaches. It verifies that all methods produce identical results and tests all-valid and all-invalid input cases. It compares `sys.getsizeof()` for a list and generator object. Results are saved in `q5_timings.csv`.

## 7.7 Alternative: Generator Expression
A generator expression can process values one at a time, for example:

`sum(value for value in readings if -50 <= value <= 50)`

Both list comprehension and generator processing take O(n) time for n readings. A list of all results uses O(n) memory; a generator uses O(1) additional iteration memory, excluding the source data.

## 7.8 Result
This task demonstrates data cleaning, temperature conversion, alarm identification and alternative Python iteration techniques. A list comprehension is concise and useful, but a generator is preferable when the full result list is not required in memory.

**Actual timings and memory values:** [Insert measurements.]  
**Output screenshot:** [Insert screenshot.]

# 8. Q6 – NESTED DATA: A RAILWAY TIMETABLE
**Marks: 7 | Level: K4 – Analyse**

## 8.1 Problem Statement
A railway enquiry counter stores a timetable as a dictionary mapping train numbers to nested dictionaries. Each train record contains a name, a list of station-arrival-departure tuples and a set of running days.

The system must find trains stopping at a specified station on a specified day, sort trains by departure time and display the timetable.

## 8.2 Data Structure Design
- Outer dictionary: train number maps to train information.
- Inner dictionary: stores name, stops and running days.
- List: preserves the ordered sequence of stops.
- Tuple: stores station, arrival and departure as one record.
- Set: stores unique running days and supports efficient membership checks.

The departure time at the third station of a train can be accessed using:

`timetable[train_number]["stops"][2][2]`

The first index selects the train, the second accesses its stops list, and the third selects the departure field of the third station tuple.

## 8.3 Station Query
A scan-based query checks every train, verifies whether it runs on the requested day, and checks each stop for the requested station.

If there are T trains and S average stops per train, a scan query takes O(T × S) time.

## 8.4 Station Index
An index maps each station to a list of trains stopping there. The index is built by scanning all timetable stops once. A query then examines only the trains associated with the requested station.

The query cost becomes proportional to the number of trains stopping at that station, rather than all stops in the timetable.

## 8.5 Experimental Investigation
The program creates timetables of 100, 1,000 and 10,000 trains. It measures index construction time, 100 scan-based queries and 100 indexed queries. It also tests an unknown station and measures the shallow size of the index dictionary. Results are saved in `q6_timings.csv`.

## 8.6 Alternative: Flat List
A flat list of `(train, station, arrival, departure, days)` tuples can be scanned for every query. This requires O(total stops) time per query. A station index requires extra memory but reduces query work to O(number of trains at the station), after the index has been built.

## 8.7 Result
The railway timetable demonstrates how nested data structures model real-world information and how an index can improve repeated station queries at the cost of additional memory.

**Actual timings and memory results:** [Insert values from q6_timings.csv.]  
**Output screenshot:** [Insert screenshot.]

# 9. Q7 – DESIGN A CONTACT-MERGING PROGRAM FROM FIRST PRINCIPLES
**Marks: 10 | Level: K5 – Evaluate**

## 9.1 Problem Statement
A user is moving to a new phone and has contacts from two old phones and a SIM card. The same person may appear multiple times with different name spellings and phone-number formats. The program must merge duplicate contacts so that each identified person appears once with all associated phone numbers and email addresses.

## 9.2 Stage 1 – Interpret the Problem
**Inputs:** Contact records from multiple sources, with fields such as name, phone number and email address.

**Output:** A merged collection in which records identified by the same normalised phone number are grouped together, retaining available names, numbers and email addresses.

**Matching rule:** Phone numbers are normalised to digits. A country prefix of 91 is removed when it appears as a 12-digit Indian number. Contacts with the same resulting number are merged.

**Data structures:**
- Dictionary: groups contacts by normalised phone number.
- Sets: retain unique phone numbers, emails and name aliases.
- Strings: store names, numbers and email addresses.

**Measurable requirements:**
1. Equivalent phone formats should normalise to the same key.
2. Duplicate numbers and emails should not be repeated.
3. Missing phone numbers should not be incorrectly merged into one person.
4. The output should retain available names and contact details.
5. The implementation should be tested on duplicate, missing-field and differently formatted records.

## 9.3 Stage 2 – Design
The program normalises phone numbers by retaining digits and handling the specified country prefix. Names are cleaned for display and alias tracking. The dictionary is keyed by the normalised phone number. Each dictionary value contains a display name and sets of numbers, emails and aliases.

### Pseudocode
1. Create an empty dictionary called merged.
2. For each source contact list:
   a. For each contact:
      i. Normalise its phone number.
      ii. If a usable phone key exists, use it as the dictionary key.
      iii. If the phone is missing, keep the record separate unless a stronger identity rule is available.
      iv. Create a new contact entry if the key is not present.
      v. Add the name to aliases when available.
      vi. Add the original phone number to the number set.
      vii. Add the lowercased email to the email set.
3. Convert grouped dictionary values into the final output list.
4. Return the merged contacts.

## 9.4 Stage 3 – Implement and Measure
The implementation tests duplicate contacts such as “Dr. Ravi” and “ravi kumar” with differently formatted versions of the same phone number. It also tests missing phone numbers and email addresses.

The program measures dictionary-based merging for 1,000 and 100,000 contacts. A pairwise comparison is measured for 1,000 contacts; the 100,000-contact pairwise test is omitted from the automated run because its quadratic growth can make it impractical. Results are saved in `q7_timings.csv`.

A small example should also be merged manually and compared with the program output.

## 9.5 Stage 4 – Defend the Design
A dictionary keyed by a normalised phone number offers average O(1) lookup and insertion. Processing n contacts therefore takes O(n) average time, excluding the cost of normalising each phone number.

Comparing every pair of contacts takes O(n²) time and becomes inefficient for large contact collections.

Two different people with the same name are not merged merely because their names match. The phone number is the primary identity key.

One limitation is that two people sharing the same phone number, or one person using multiple different phone numbers, may be incorrectly separated or merged. A more advanced system could use multiple verified identifiers and a manual review process.

## 9.6 Alternative: Pairwise Comparison
The alternative compares every contact with existing contacts to find duplicates. In the worst case, it requires O(n²) comparisons. The dictionary approach requires O(n) average processing time and O(n) storage for the merged records. The pairwise method may use less auxiliary indexing memory but has much higher processing cost.

## 9.7 Result
The contact-merging system demonstrates data-structure design from requirements. Normalised dictionary keys provide efficient grouping, while sets prevent repeated phone numbers, email addresses and aliases.

**Actual timings:** [Insert values from q7_timings.csv.]  
**Output screenshot:** [Insert screenshot.]

# 10. OVERALL ANALYSIS AND LEARNING OUTCOMES

The seven tasks demonstrate different data structures and their appropriate applications.

| Question | Main Data Structure / Concept | Application |
|---|---|---|
| Q1 | Lists and slicing | Rainfall records |
| Q2 | Tuples, mutability and copying | Bus-stop coordinates and passenger grid |
| Q3 | Dictionaries | Farmer complaint analysis |
| Q4 | Sets | Elective registration clashes |
| Q5 | List comprehension | Sensor reading cleaning |
| Q6 | Nested data structures | Railway timetable |
| Q7 | Dictionary and sets | Contact merging |

## 10.1 Key Complexity Summary
- List indexing: O(1); insertion at an arbitrary position: O(n).
- Tuple indexing: O(1); tuples are immutable at the outer level.
- Dictionary lookup: O(1) average.
- Set membership: O(1) average.
- List membership: O(n).
- Dictionary word counting: O(n) average over n tokens.
- Set operations: O(n + m) expected for sets of sizes n and m.
- List comprehension: O(n) time for n input elements.
- Indexed railway query: proportional to the number of trains at the station.
- Dictionary-based contact grouping: O(n) average, assuming expected constant-time dictionary operations.

## 10.2 Learning Outcomes
After completing the assignment, the student gains practical experience in:
1. Selecting suitable data structures for different applications.
2. Manipulating lists using indexing and slicing.
3. Understanding tuple immutability and hashability.
4. Identifying aliasing and copying issues.
5. Counting and grouping data using dictionaries.
6. Applying set operations to remove duplicates and identify overlaps.
7. Cleaning data using list comprehensions, map and filter.
8. Designing nested data structures.
9. Creating indexes to accelerate queries.
10. Designing a data-merging solution from requirements.
11. Measuring execution time and memory.
12. Comparing algorithms using Big-O notation.

# 11. GITHUB SUBMISSION AND VERSION CONTROL

The required repository name is:

`CSA08-RegisterNumber-Assignment3`

The repository must contain one folder per task, Python source files, input files where applicable, output screenshots, README.md and requirements.txt.

At least one progressive commit must be made for each task. The repository must be shared with the course faculty as public or private with the faculty added as a collaborator.

Suggested commit messages:
1. Add Task01 – Rainfall Lists and Slicing
2. Add Task02 – Tuples and Copying
3. Add Task03 – Farmer Complaint Dictionaries
4. Add Task04 – Elective Registration Sets
5. Add Task05 – Sensor List Comprehensions
6. Add Task06 – Railway Nested Timetable
7. Add Task07 – Contact Merger Design
8. Add final report and evidence

# 12. CONCLUSION

This assignment provided practical experience in selecting and applying Python data structures to real-world problems.

The rainfall analysis task demonstrated list operations and slicing. The bus-stop task explained tuple immutability, aliasing and copying. The farmer helpline task demonstrated dictionary-based frequency counting and grouping. The elective registration task showed how sets efficiently identify duplicates and registration clashes.

The sensor monitoring task applied list comprehensions and functional transformations. The railway timetable task demonstrated how nested data structures and indexing support organised storage and faster queries. Finally, the contact-merging task applied first-principles design using normalised dictionary keys and sets.

The experimental investigations highlighted the importance of measuring execution time and memory rather than relying only on theoretical assumptions.

Overall, the assignment improved understanding of Python data structures, algorithmic efficiency, problem-solving, testing and software design.

# 13. APPENDIX – EXECUTION EVIDENCE

Attach the following evidence:

**Appendix A – Q1**
- Rainfall list and weekly totals.
- Wettest and driest reading positions.
- Moving-average output.
- Dry-day list.
- Naive versus running-sum timing results.

**Appendix B – Q2**
- Incorrect shared-row grid output.
- Correct independent-row grid output.
- Tuple dictionary-key output.
- Aliasing and shallow/deep copy output.
- Memory and indexing measurements.

**Appendix C – Q3**
- Word-frequency output.
- Top-k word results.
- District grouping output.
- Dictionary, list.count and Counter timing results.

**Appendix D – Q4**
- Clash, exactly-one and neither outputs.
- Set membership timing results.
- Empty and identical elective test results.
- Venn diagram.

**Appendix E – Q5**
- Loop, comprehension and map/filter outputs.
- Alarm-minute results.
- Execution-time comparison.
- List and generator memory comparison.

**Appendix F – Q6**
- Nested timetable output.
- Station query results.
- Indexed query results.
- Query timing and index memory results.

**Appendix G – Q7**
- Contact input examples.
- Normalised and merged output.
- Manual verification.
- Dictionary and pairwise timing comparison.

---

**GitHub Repository Link:** ______________________________

**Student Name:** ______________________________________

**Register Number:** ____________________________________

**Date:** ______________________________________________

**END OF REPORT**
