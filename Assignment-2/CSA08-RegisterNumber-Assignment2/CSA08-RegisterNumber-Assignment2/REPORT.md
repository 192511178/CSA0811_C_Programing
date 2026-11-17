# PYTHON PROGRAMMING – ASSIGNMENT 2
**SIMATS Online Lab | Course Code: 192511178C**  
**Title:** Control Flow, Strings and Functions  
**Total:** 50 Marks

## Student Details
- Name: [Enter name]
- Register Number: [Enter register number]
- Department: [Enter department]
- Python version: [Enter actual version]

## 1. Introduction
This assignment applies Python control-flow constructs, loops, string operations, functions and recursion to practical problems. Each task involves understanding requirements, designing a solution, implementing it, executing tests and analysing results.

## 2. Q1 – Decisions with Many Boundaries (6 marks)
**Objective:** Determine electricity subsidy eligibility using unit consumption, ration-card status and the senior-citizen condition.

**Rules from the assignment:** 100 units or less receives subsidy; 101–200 units receives partial subsidy only with a ration card; above 200 units receives no subsidy unless a household member is above 80 years.

**Concepts:** separate `if`, `if-elif-else`, chained comparisons, Boolean `and`/`or`, nested conditions.

**Algorithm:** Read units and household conditions; check the consumption range; check the additional condition where required; display the decision.

**Testing:** Include eight household predictions and explicitly test 100, 101, 200 and 201 units. Compare the separate-if implementation with the if-elif-else implementation. Separate independent conditions can each execute; an if-elif-else chain selects the first matching branch.

**Alternatives:** `match-case` (Python 3.10+) and a lookup list of upper limits searched in a loop.

**Complexity:** A chain or lookup over k categories is O(k) worst case; constant auxiliary space for direct decisions. A lookup list occupies O(k) storage.

**Actual output / observations:** [Paste your output and explain it here.]

## 3. Q2 – Loops that Count Attempts (4 marks)
**Objective:** Implement bank-kiosk OTP verification with three attempts. Blank entries do not count. Three wrong attempts lock the account for 30 minutes. A correctly answered security question adds two attempts.

**Concepts:** `while`, `for range(3)`, `break`, `continue`, `pass`, loop `else`.

**Algorithm:** Request an OTP; ignore blank entries; accept a correct OTP and stop; count incorrect nonblank entries; lock after the allowed attempts are exhausted.

**Comparison:** `while` is natural when the number of valid attempts depends on user input and blank input must be re-entered. `for` is suitable for a fixed attempt limit. Incorrect counter placement can cause blank input to count or can create an infinite loop.

**Alternative:** Recursion can request the next attempt, but it uses O(a) call-stack space. Loop solutions use O(1) auxiliary space. Time is O(a), where a is the number of attempts.

**Actual output / observations:** [Paste output for correct OTP, wrong OTP, blank entry and exhausted attempts.]

## 4. Q3 – Vehicle Registration Number Validator (6 marks)
**Objective:** Normalise, validate and format registration strings. Required structure: two letters, two digits, one or two letters, four digits.

**Allowed string operations:** indexing, slicing, `len()`, `upper()`, `replace()`, `strip()`, `isalpha()`, `isdigit()`, `split()` and `join()`. Regular expressions are not used in the main implementation.

**Algorithm:** Strip outer whitespace, remove spaces and hyphens, uppercase the text, check total length, validate each character group, then format as `TN 09 AB 1234`.

**Expected examples:** `tn 09 ab 1234` → `TN09AB1234` valid; `KA-01-M-0007` → `KA01M0007` valid; `TN9AB1234` invalid; `TN 22 1234 AB` invalid.

**String immutability:** String methods return new strings rather than changing the original string. `s[-4:]` extracts the last four characters; `s[4:-4]` extracts the middle section after the first four and before the last four characters.

**Alternative:** `re.fullmatch()` can validate the complete pattern, but the assignment's primary solution must not use regex.

**Complexity:** Normalisation, validation and formatting are O(L) in the input length; temporary string storage is O(L).

**Actual output / observations:** [Paste output and explain valid/invalid cases.]

## 5. Q4 – Building Long Text: + or join()? (6 marks)
**Objective:** Compare repeated `+=`, list plus `''.join()` and f-string line generation for 1,000, 10,000 and 200,000 records.

**Concepts:** string immutability, concatenation, `join()`, f-strings, `time.perf_counter()`.

**Method:** Run each approach three times for each input size. Record each time and calculate average = (trial 1 + trial 2 + trial 3) / 3.

**Analysis:** `join()` is generally recommended for combining many fragments because it constructs the combined string efficiently. Repeated concatenation can approach quadratic work in the total number of fragments; CPython may optimise some `+=` cases, so measured results depend on implementation and environment. f-strings format each individual record; they do not alone define how all records are combined.

**Alternatives:** Write records directly to a file or use `io.StringIO`.

**Complexity:** `join()` is linear in total output size. Repeated `+=` can approach O(n²) for similarly sized fragments. Direct writing and StringIO are typically linear in total data processed.

**Measurement table:** Paste the generated `performance_results.csv` values and discuss the actual averages. Do not invent timings.

## 6. Q5 – Functions, Parameters and Scope (7 marks)
**Objective:** Build a canteen order function and explain the mutable-default-parameter problem.

**Bug:** A list used as a default parameter is created once when the function is defined and can be shared across calls.

**Correction:** Use `None` as the default and create a new list inside the function when the argument is `None`.

**Concepts:** positional, keyword and default parameters; multiple return values; local, global and nonlocal scope; `global` keyword; `__defaults__`.

**Alternatives:** Require the caller to pass a list, or use a closure to maintain order state.

**Complexity:** Appending one item to a list is O(1) amortised; storing n items requires O(n) space.

**Actual output / observations:** [Paste output showing shared default and independent corrected lists.]

## 7. Q6 – Recursion and Its Limits (8 marks)
**Objective:** Count ways to climb n steps when each move is one or two steps.

**Recurrence:** W(n) = W(n−1) + W(n−2), with W(0) = 1 and W(1) = 1.

**Expected values:** n=1..6 gives 1, 2, 3, 5, 8, 13.

**Methods:** Naive recursion, memoisation using `functools.lru_cache`, and an iterative alternative.

**Analysis:** Naive recursion has exponential time, commonly expressed O(phi^n), and O(n) stack depth. Memoisation reduces time to O(n), with O(n) cache and stack space. Iteration uses O(n) time and O(1) auxiliary space.

**Recursion limit:** Report `sys.getrecursionlimit()` and test `ways_memo(1000)`. Memoisation removes repeated computation but does not eliminate Python's recursion-depth limit.

**Measurements:** Include call counts for n=10, 20, 25 and 30, and explain the difference between naive and memoised calls.

**Actual output / observations:** [Paste your results.]

## 8. Q7 – Diagnose, Redesign and Validate (13 marks)
**Selected program:** Q6 staircase counting.

**A. Diagnose:** Naive recursion recalculates the same subproblems, causing exponential growth in work.

**B. Objective:** Preserve correct answers while reducing calls and execution time.

**C. Redesign:** Use memoisation to store previously computed results. Pseudocode: if result is cached, return it; if n is a base case, return 1; otherwise calculate W(n−1)+W(n−2), store and return it.

**Memory trade-off:** Memoisation uses O(n) cache space and O(n) stack space, while reducing time to O(n). An iterative implementation avoids recursive stack use and uses O(1) auxiliary space.

**D. Prediction:** Fewer repeated calls and faster execution for larger n, with additional cache memory.

**E. Validation:** Run original, memoised and iterative implementations on identical inputs. Confirm that all produce the same answer. Record execution time and call counts.

**F. Defence:** Memoisation is appropriate when repeated subproblems occur. Iteration is preferable when recursion depth is a concern.

**Actual comparison:** [Paste your measured results and explain whether the objective was achieved.]

## 9. Overall Conclusion
The seven tasks demonstrate Python decision structures, loop control, string processing, functions, scope, recursion, performance measurement and optimisation. The assignment reinforces the complete problem-solving cycle: predict, design, implement, measure, analyse, evaluate, redesign and validate.

## 10. Evidence checklist
- [ ] Eight Q1 household predictions and four boundary tests
- [ ] Q2 while and for implementations and control-statement demonstrations
- [ ] Q3 normalisation, validation and formatter outputs
- [ ] Q4 three trials, averages and performance comparison
- [ ] Q5 mutable default and corrected function outputs
- [ ] Q6 n=1..6 results, call counts and recursion-limit test
- [ ] Q7 original-versus-redesigned measurements
- [ ] Output screenshots and GitHub repository link
