

import shutil
from pathlib import Path

# Set the current VS Code folder as the project root
PROJECT = Path.cwd()
print(f"Setting up project in: {PROJECT}")

# 1. Create folders
FOLDERS = ['data/raw', 'data/processed', 'src', 'results/tables', 'results/figures', 'docs', 'notebooks']
for folder in FOLDERS:
    (PROJECT / folder).mkdir(parents=True, exist_ok=True)

# 2. Move any existing data files from Lab 1 to data/raw/
moved = []
data_dir = PROJECT / "data"
if data_dir.exists():
    for item in sorted(data_dir.iterdir()):
        if item.is_file() and item.name != "README.md":
            target = PROJECT / "data" / "raw" / item.name
            if not target.exists():
                shutil.move(str(item), str(target))
                moved.append(f"Moved {item.name} to data/raw/")

# 3. Define file contents
FILES = {
    'data/raw/README.md': '# data/raw/\n\nOriginal data files exactly as downloaded or created. Never edit them by hand.\n',
    'data/processed/README.md': '# data/processed/\n\nData produced by YOUR code.\n',
    'src/README.md': '# src/\n\nPython modules (.py) – one module per step of the project.\n',
    'results/tables/README.md': '# results/tables/\n\nResult tables saved by your code (CSV / JSON).\n',
    'results/figures/README.md': '# results/figures/\n\nPlots saved by your code (PNG).\n',
    'docs/README.md': '# docs/\n\nDescription of the project: concept, data dictionary, block diagram.\n',
    'notebooks/README.md': '# notebooks/\n\nLab worksheets and experiments (optional).\n',
    'src/__init__.py': '"""Project package – one module per step of the project (see README.md)."""\n',
    'src/stats.py': '"""stats.py – Lab 3: functions that compute numbers from your data."""\n\n# Your code from Lab 3 goes below.\n',
    'src/models.py': '"""models.py – Lab 4: classes that describe the "things" in your data."""\n\n# Your code from Lab 4 goes below.\n',
    'src/cleaning.py': '"""cleaning.py – Lab 5: find and handle bad data."""\n\n# Your code from Lab 5 goes below.\n',
    'src/storage.py': '"""storage.py – Lab 6: files, folders and saving results."""\n\n# Your code from Lab 6 goes below.\n',
    'src/viz.py': '"""viz.py – Lab 7: NumPy calculations and plots."""\n\n# Your code from Lab 7 goes below.\n',
    'docs/project_concept.md': '# Project concept\n\nFill in every section. Write for a person who knows nothing about your topic.\n',
    'docs/data_dictionary.md': '# Data dictionary\n\n**File:** `data/raw/my_data.csv`\n',
    '.gitignore': '.ipynb_checkpoints/\n__pycache__/\ndata/raw/*.zip\n',
    'README.md': '# Project title\n\n**Team:** name (GitHub: @login), name, name\n'
}

LOADER = '''"""loader.py – Lab 2: get the raw data into Python."""
import csv
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = PROJECT_DIR / "data" / "raw"
PROCESSED_DIR = PROJECT_DIR / "data" / "processed"

_ENCODINGS = ("utf-8-sig", "cp1250", "latin-1")
_MISSING = {"", "na", "n/a", "nan", "none", "null", "-", "?"}

def _detect_delimiter(header_line):
    candidates = [",", ";", "\\t", "|"]
    counts = {sep: header_line.count(sep) for sep in candidates}
    best = max(counts, key=counts.get)
    return best if counts[best] > 0 else ","

def load_csv(path, delimiter=None, encoding=None):
    path = Path(path)
    if not path.is_absolute() and not path.exists():
        path = RAW_DIR / path
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    encodings = (encoding,) if encoding else _ENCODINGS
    for enc in encodings:
        try:
            text = path.read_text(encoding=enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError("csv", b"", 0, 1, f"cannot decode {path.name}")

    lines = text.splitlines()
    if not lines:
        return []
    sep = delimiter or _detect_delimiter(lines[0])
    reader = csv.DictReader(lines, delimiter=sep)
    reader.fieldnames = [name.strip() for name in reader.fieldnames]
    rows = []
    for row in reader:
        if any(value not in (None, "") for value in row.values()):
            rows.append({key: (value or "").strip() for key, value in row.items() if key})
    return rows

def to_number(text):
    if text is None: return None
    if isinstance(text, (int, float)): return float(text)
    text = str(text).strip().replace(" ", "").replace(",", ".")
    if text.lower() in _MISSING: return None
    try: return float(text)
    except ValueError: return None

def to_bool(text):
    value = str(text).strip().lower()
    if value in ("true", "t", "yes", "y", "1"): return True
    if value in ("false", "f", "no", "n", "0"): return False
    return None

def _convert(value, kind):
    if kind is bool: return to_bool(value)
    if kind is int:
        number = to_number(value)
        return None if number is None else int(number)
    if kind is float: return to_number(value)
    text = str(value).strip()
    return None if text.lower() in _MISSING else text

def convert_rows(rows, column_types):
    return [{name: _convert(row[name], kind) for name, kind in column_types.items()} for row in rows]

def get_column(rows, name, skip_missing=True):
    values = [row[name] for row in rows]
    return [v for v in values if v is not None] if skip_missing else values

# ===========================================================================
# PART B – YOUR PROJECT SETTINGS (fill in during Lab 2)
# ===========================================================================
DATA_FILE_NAME = "my_data.csv"      

COLUMN_TYPES = {
}

def load_project_data():
    return convert_rows(load_csv(DATA_FILE_NAME), COLUMN_TYPES)
'''

FILES['src/loader.py'] = LOADER

# 4. Write files if they do not exist
created = []
for rel, text in FILES.items():
    path = PROJECT / rel
    if not path.exists():
        path.write_text(text, encoding="utf-8")
        created.append(rel)

print("✅ Setup complete.")
for line in moved: print(f"   {line}")
for rel in created: print(f"   created {rel}")