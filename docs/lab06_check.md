# Lab 6 – result check (2026-11-20)

**Result: 6/6**

- [OK] Part 2 – try/except, raise, debugging, generator, decorator (TEST DATA)
- [OK] src/loader.py – your own to_number and to_bool, your data loads
- [OK] src/cleaning.py – check_row, valid_rows, @timed clean + rules for your columns
- [OK] main.ipynb uses src.cleaning (clean_rows, report)
- [OK] main.ipynb runs from top to bottom
- [OK] Finding + three explanations (at least 8 words each)

## FINDING
the cleaning removed only 3 rows out of our data (the dataset we used was really clean). They were removed because of missing Financial Stress Values, so our main results were left unchanged.

## EXPLAIN_TRY
to_number try/except attempts to convert the cleaned text into float. The exception is used when it's not a value that can be converted to float and then its just replaced by  (instead of crashing bcs invalid)

## EXPLAIN_GENERATOR
a normal function with a return processes all at once (the whole list) which builds a whole thing in our memory at once and can lead to crashes due to using all the RAM we have if the list is too big. Yield solves this issue bcs it pauses and only hands over 1 row at a time so no memory overload

## EXPLAIN_DECORATOR
calling clean with the wrapper function @timed measures the execution time using pref_counter, then it prints the duration and returns the result of our function
