import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

employee_data = pd.DataFrame({
    'employee_id': ['E01', 'E02', 'E03', 'E04', 'E05', 'E06', 'E07', 'E08'],
    'name': ['Liza', 'Mark', 'Rico', None, 'Ana', 'Ben', 'Jen', 'Carlo'],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', None, 'HR', 'Sales'],
    'salary': [45000, 62000, None, 55000, 70000, 52000, 48000, None],
    'years_experience': [3, 5, 4, None, 8, 6, 2, 3],
    'performance_score': [4.2, 4.5, 3.8, 4.0, np.nan, 3.9, 4.3, 4.1]
})

"""
Print the full True/False missingness frame.

Print whether each column has any missing values.

Print the count of missing values per column.

Create a bar plot of the missing counts per column, with a title 'Missing Values by Column' and y-label 'Count'. Display it.

In one sentence: which column has the most missing values, and what does that tell you about where to start cleaning?
"""
print(employee_data.isna())
print('--------------------------------------------------------')
print(employee_data.isna().any())
print('--------------------------------------------------------')
print(employee_data.isna().sum())

employee_data.isna().sum().plot(
    kind='bar',
    ylabel='Count'
)
plt.show()