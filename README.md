# Cookie Log Analyzer

A Python program to find the **most active cookie(s)** for a given date from a CSV log file.  

---

## Installation

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/) installed on your system.  
- No external dependencies are required — only Python’s standard library is used.

You can confirm Python is installed with:

```bash
python3 --version
```

---

## Usage

### Run the program

```bash
python3 process.py -f cookies.csv -d 2018-12-09
```

- `-f` : Path to the CSV log file.  
- `-d` : Target date in **UTC** (format `YYYY-MM-DD`).  

Example output (each cookie printed on a new line):

```
AtY0laUfhglK3lC7
```

If multiple cookies are tied for most active, all of them are printed:

```
SAZuXPGUrfbcn5UA
4sMM2LxV07bPJzwf
fbcn5UAVanZf6UtG
```

---

## Running Tests

All tests (unit + integration) are written using Python’s built-in **unittest** framework.

### Run all tests

From the project root:

```bash
python3 -m unittest discover tests
```

This will automatically discover and run all test files inside the `tests/` directory.

### Run a specific test file

```bash
python3 -m unittest tests/test_validate.py
```

---

## Project Structure

```
project/
│── process.py              # Main program
│── tests/                  # Test suite
│   ├── test_validate.py    # Tests for validate_file, validate_date
│   ├── test_parse_cli.py   # Tests for CLI parsing
│   ├── test_compare.py     # Tests for compare_dates
│   ├── test_count.py       # Tests for count_cookies
│   ├── test_active.py      # Tests for most_active_cookies
│   ├── test_print.py       # Tests for print_results
│   └── test_integration.py # End-to-end integration tests
└── README.md
```

---

## To Note:

- We assume that theinput log file must be a **CSV file** with headers:
  ```
  cookie,timestamp
  ```
- Timestamps are expected in **ISO format** (e.g. `2018-12-09T10:00:00+00:00`).  
- The program assumes the log file is **sorted by timestamp (descending)** for early stopping optimization.
- Test coverage can be found by installing coverage package. Run this command to generate a coverage report.
  ```
  coverage run -m unittest discover tests
  ```
- To view the coverage report run this command - 
  ```
  coverage report -m
  ```

