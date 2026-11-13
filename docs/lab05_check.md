# Lab 5 – result check (2026-11-13)

**Result: 6/6**

- [OK] Part 2 – classes, methods, overloading, inheritance, polymorphism (TEST DATA)
- [OK] Part 3 – Dataset, Analysis family, Filter family (TEST DATA)
- [OK] src/models.py – Dataset, CountBy, GroupMean, TopGroups, Filter, Equals, Above work
- [OK] main.ipynb uses src.models (objects of your classes)
- [OK] main.ipynb runs from top to bottom
- [OK] Finding + two explanations (at least 8 words each)

## Finding
Our analysis shows that while the mean CGPA is similar for all of the sleeping times in the whole dataset, among the top students (with CGPA > 8.0) the majority sleeps 7-8 or more hours

## What is self
Its pointing to our own object. For us it's if we use eg. self.rows, we are telling the method to read the rows belonging to our exact dataset (the one that is our object)

## Inheritance and polymorphism
TopGroups inherits after GroupMean, to use its function (mean value calculation) so it can sort it instead of writing both mean and sort functions from the beginning. Polimorphism allows us to run different analyses on 1 loop, because each analysis has its own function report(), so the loop only calls report() and the object knows what to do by itself
