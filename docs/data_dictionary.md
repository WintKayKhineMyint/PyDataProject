# Data dictionary

**File:** `data/raw/Student_Depression_Dataset.csv`

| Column | Meaning | Type in Python | Unit / values | Used? | Why |
|---|---|---|---|---|---|
| id | Student identifier | int | number | no | Does not provide analytical value |
| Gender | Student gender | str | Male/Female | yes | To see if stressors affect genders differently |
| Age | Student age | int | years | yes | To check if age impacts stress levels |
| City | Home city | str | text | no | Geography is outside our current scope |
| Profession | Current occupation | str | text | no | Assuming all rows are students based on dataset |
| Academic Pressure | Study stress level | int | 1-5 scale | no | Focusing specifically on financial stress instead |
| Work Pressure | Job stress level | int | 1-5 scale | no | Not part of our core question |
| CGPA | Academic performance | float | 1.0 - 10.0 | yes | The main academic metric to track |
| Study Satisfaction | Course satisfaction | int | 1-5 scale | no | Secondary to CGPA for this scope |
| Job Satisfaction | Work satisfaction | int | 1-5 scale | no | Not relevant for a student-focused analysis |
| Sleep Duration | Average nightly sleep | str | text ranges | yes | Core variable to correlate with depression |
| Dietary Habits | Diet quality | str | text | no | Focusing strictly on sleep and finances |
| Degree | Current study level | str | text | no | Broad demographic not needed right now |
| Have you ever had suicidal thoughts ? | Suicidal ideation | str | Yes/No | no | Sticking strictly to the primary Depression indicator |
| Work/Study Hours | Daily working hours | float | hours | no | Using Sleep Duration as our main time-based metric |
| Financial Stress | Money anxiety | int | 1-5 scale | yes | Core variable to measure environmental stress |
| Family History of Mental Illness | Genetic predisposition | str | Yes/No | no | Looking purely at lifestyle and environmental factors |
| Depression | Mental health status | bool | True/False | yes | The target variable for our analysis |