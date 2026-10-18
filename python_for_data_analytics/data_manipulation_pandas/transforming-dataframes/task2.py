import pandas as pd

employees = pd.DataFrame({
    'name': ['Liza', 'Mark', 'Rico', 'Jen', 'Ana', 'Ben'],
    'department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'HR'],
    'salary': [45000, 62000, 48000, 55000, 70000, 52000]
})

"""
    Sort by salary in descending order. Save as by_salary and print the head.
    Sort by department ascending, then salary descending. Save as by_dept_salary and print the head.
"""
by_salary = employees.sort_values('salary', ascending=False)
print(f"by salary descending: {by_salary.head()}")
by_dept_salary = employees.sort_values(['department','salary'],ascending=[True,False])
print(f"by department salary descending: {by_dept_salary.head()}")