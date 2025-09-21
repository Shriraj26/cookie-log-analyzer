import tempfile
import csv

def _make_csv(rows):
    """
    A utility function to create a mock CSV file. This
    returns a path to that temp file.
    """
    tmp = tempfile.NamedTemporaryFile(mode="w", delete=False, newline="")
    writer = csv.writer(tmp)
    writer.writerow(["cookie", "timestamp"])  # header
    writer.writerows(rows)
    tmp.close()
    return tmp.name