import pandas as pd

employees = pd.DataFrame({
    'employee_id': ['E101', 'E102', 'E103', 'E104'],
    'name': ['Liza', 'Mark', 'Rico', 'Jen'],
    'department': ['Sales', 'IT', 'Sales', 'HR'],
    'salary': [45000, 62000, 48000, 55000]
})
"""
    task:
        Print the DataFrame's values as a NumPy array.
        Print the column names.
        Print the row index.
        In one sentence: does .columns need parentheses or not, and why?
"""
print(employees.to_numpy())
print(employees.columns)
print(employees.index)