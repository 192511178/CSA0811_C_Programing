from attendance.reader import read_records
from attendance.stats import percentage
from attendance.report import write_report

if __name__ == "__main__":
    print("Package organisation:", percentage(18, 20))
