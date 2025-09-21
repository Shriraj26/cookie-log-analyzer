import argparse
from argparse import Namespace
import csv
from datetime import datetime
import collections
import os

DATE_FORMAT = "%Y-%m-%d"

def validate_file(file_path: str) -> str:
    """
    Validate that the given file path exists.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: The validated file path.

    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"Error: File not found -> {file_path}")
    return file_path

def validate_date(date_str: str) -> str:
    parts = date_str.split("-")
    if len(parts) != 3:
        raise ValueError(f"Error: Date must be in format YYYY-MM-DD, got '{date_str}'")

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        raise ValueError(f"Error: Date must contain only digits, got '{date_str}'")

    year, month, day = int(year), int(month), int(day)

    if not (1 <= month <= 12):
        raise ValueError(f"Error: Month must be between 1 and 12, got {month}")

    if not (1 <= day <= 31):  # still need to check valid days for each month
        raise ValueError(f"Error: Day must be between 1 and 31, got {day}")

    # Final validation with datetime to catch edge cases like Feb 30
    try:
        datetime(year, month, day)
    except ValueError:
        raise ValueError(f"Error: Invalid calendar date, got '{date_str}'")
    return date_str

def parse_cli() -> Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: An object with attributes:
            - file (str): Path to the CSV log file.
            - date (str): Target date in UTC (YYYY-MM-DD).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=True, help="CSV file path")
    parser.add_argument("-d", "--date", required=True, help="Date in UTC format")
    return parser.parse_args()

def compare_dates(date_str: str, timestamp_str: str) -> int:
    """
    Compare a input date (YYYY-MM-DD) with the timestamp's date.

    Returns:
         -1 if input_date > timestamp_date
         0 if input_date == timestamp_date
         1 if input_date < timestamp_date
    """
    input_date = datetime.strptime(date_str, DATE_FORMAT).date()
    # Parse the timestamp (timezone-aware)
    ts_date = datetime.fromisoformat(timestamp_str).date()
    
    if input_date > ts_date:
        return 1
    elif input_date == ts_date:
        return 0
    else:
        return -1

def count_cookies(file_name, input_date) -> dict[str, int]:
    """
    Count cookie occurrences for a given date in the log file.

    Args:
        file_name (str): Path to the CSV log file.
        input_date (str): Target date in UTC, in YYYY-MM-DD format.

    Returns:
        dict: A mapping {cookie_id: count} for all cookies on the given date.
    """
    cookie_map = collections.defaultdict(int)
    with open(file_name, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        for cookie_id, timestamp in csvreader:
            cmp = compare_dates(input_date, timestamp)
            if cmp == 0:
                cookie_map[cookie_id] += 1
            elif cmp > 0: # Assuming log file is sorted by timestamp
                break
    
    return cookie_map

def most_active_cookies(cookie_map: dict[str, int]) -> list[str]:
    """
    Find all cookies with the highest frequency in the given mapping.

    Args:
        cookie_map (dict[str, int]): Mapping of cookie_id -> count.

    Returns:
        list[str]: List of cookie IDs that have the maximum count.
    """
    if not cookie_map:
        return []
    
    max_count = max(cookie_map.values())
    return [key for key,val in cookie_map.items() if val == max_count]

def print_results(cookie_list: list[str])->None:
    for cookie_id in cookie_list:
        print(cookie_id)    

def main():
    args = parse_cli()
    file_name = validate_file(args.file)
    input_date = validate_date(args.date)
    
    cookie_map = count_cookies(file_name, input_date)
    cookie_list = most_active_cookies(cookie_map)
    print_results(cookie_list)
        
if __name__ == "__main__":
    main()

