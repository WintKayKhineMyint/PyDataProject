# Lab 4 result check – 6/6

Generated: 2026-11-06 19:42

- ✅ loader.py understood + recursion (parts 2–3): 21/21 ✅
- ✅ src/stats.py: 4 functions for everyone: mean ✓, median ✓, count_by ✓, group_stat ✓
- ✅ src/stats.py: at least 2 from the menu: top, summary_by
- ✅ main.ipynb uses your stats.py: count_by, group_stat, summary_by, top
- ✅ main.ipynb runs from top to bottom: ok
- ✅ your finding and explanations: ok

## My first finding

Our analysis of the student depression dataset shows that CGPA distribution is extremely similar across both genders. The mean CGPA scores vary by less than a tenth of a point between groups (7.6 and 7.7).

## Explanations

convert_rows goes through every row of the CSV file. It then makes a new row out of each, but with the correct types of each column instead of plaintext

This module has our functions that show some statistics. It helps to analyse our dataset. Has functions that eg. calculate the mean, count, or group statistics
