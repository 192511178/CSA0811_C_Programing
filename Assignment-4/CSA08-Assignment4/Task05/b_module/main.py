"""Task 5(b): Main script importing one utility module."""
from attendance_utils import read_records, percentage, write_report

if __name__ == "__main__":
    print("Module organisation:", percentage(18, 20))
