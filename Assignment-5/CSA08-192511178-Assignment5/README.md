# SIMATS Python Programming – Assignment 5 (CO5)

**Student:** Mohamed Syed Thowfiq S  
**Register Number:** 192511178  
**Repository:** `CSA08-192511178-Assignment5`

## Overview
This repository follows the Assignment 5 case study: City Air-Quality Monitoring Network.
It contains designs and runnable Python examples for data acquisition, cleaning, SQLite,
visualisation, debugging/profiling, citizen-complaint analysis, adversarial testing,
performance comparison and the final engineering decision.

## Requirements
- Python 3.10+
- pandas
- matplotlib

Install:
```bash
python -m pip install -r requirements.txt
```

## Run
Run each script from the repository root, for example:
```bash
python Task01/data_acquisition.py
python Task02/clean_normalise.py
python Task03/analysis_visualisation.py
python Task04/debug_profile.py
python Task05/complaint_ai.py
python Task06/cleaning_pipeline.py
python Task07/adversarial_sql.py
python Task08/loops_pandas_sql.py
python Task09/final_decision.py
```

Scripts create sample inputs, SQLite databases, reports and charts in their task folders.
Replace illustrative data and timing placeholders with actual measurements from your computer
before submission. Add screenshots of your own executions to the relevant task folders.

## Libraries
- Python standard library: csv, sqlite3, statistics, re, logging, time, timeit, cProfile, pathlib
- pandas
- matplotlib

## Task results
- Task01: Inspects CSV sources and creates SQLite station/readings tables.
- Task02: Applies missing-value, range, duplicate and temperature-unit rules.
- Task03: Creates daily summaries and air-quality charts.
- Task04: Demonstrates logging, assertions, timing and profiling.
- Task05: Implements lexicon sentiment scoring, extractive summarisation and a rule-based chatbot.
- Task06: Runs the required CSV cleaning pipeline and min-max normalisation.
- Task07: Tests adversarial CSV input and safe parameterised SQL.
- Task08: Compares loops, Pandas and SQL aggregation.
- Task09: Demonstrates complaint scoring, indexing and production recommendations.

## Submission reminder
The assignment requires progressive commits, executed code, input/output evidence, charts,
timing/profile output and results from at least 50 complaints. The included sample data is
for demonstration; run the scripts and add your own measured evidence.
