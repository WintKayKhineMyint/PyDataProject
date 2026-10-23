"""Loading data files.

Lab 1: a ready-made helper, so you can look at your data today.
Lab 2: you will extend this module yourself (types, conversions, your own loader).
"""
import csv
from pathlib import Path


def load_csv(path, delimiter=None, encoding="utf-8-sig"):
    """Read a CSV file and return a list of rows.

    Every row is a dictionary: {column name: value}.
    All values are returned as text (str) - converting them is your job.

    path      -- file to read (str or Path)
    delimiter -- column separator; None = detect automatically (",", ";" or tab)
    encoding  -- try "cp1250" or "latin-1" if you see strange characters
    """
    path = Path(path)
    with path.open(newline="", encoding=encoding) as f:
        sample = f.read(4096)
        f.seek(0)
        if delimiter is None:
            try:
                delimiter = csv.Sniffer().sniff(sample, delimiters=",;\t").delimiter
            except csv.Error:
                delimiter = ","
        return list(csv.DictReader(f, delimiter=delimiter))
