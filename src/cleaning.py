"""cleaning.py – Lab 5: find and handle bad data."""

# Your code from Lab 5 goes below.
import time


def check_row(row, required, non_negative):
    for column in required:
        if row[column] is None:
            raise ValueError(f"{column} is missing")
    for column in non_negative:
        if row[column] is not None and row[column] < 0:
            raise ValueError(f"{column} is negative")


def valid_rows(rows, report, required, non_negative):
    for row in rows:
        try:
            check_row(row, required, non_negative)
        except ValueError as e:
            message = str(e)
            report[message] = report.get(message, 0) + 1
            continue
        yield row


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f} s")
        return result
    return wrapper


@timed
def clean(rows, required, non_negative):
    report = {}
    kept = list(valid_rows(rows, report, required, non_negative))
    return kept, report


REQUIRED = ["Age", "Gender", "CGPA", "Sleep Duration", "Financial Stress", "Depression"]
NON_NEGATIVE = ["Age", "CGPA", "Financial Stress"]