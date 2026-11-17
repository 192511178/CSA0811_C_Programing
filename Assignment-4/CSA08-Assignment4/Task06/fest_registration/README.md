# College Fest Registration Desk

Run from this folder:
`python run_fest.py`

The script creates sample department files, processes clean, duplicate, invalid-email and damaged records, logs an expected missing department file, and writes:
- output/master_list.csv
- output/event_*.csv
- output/summary.txt
- output/error_log.csv

Email validation uses string methods as requested. This is a basic format check, not full RFC email validation.
