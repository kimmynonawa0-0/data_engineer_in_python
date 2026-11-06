import pandas as pd

sales_data = pd.DataFrame({
    'region': ['Luzon', 'Luzon', 'Luzon', 'Luzon',
               'Visayas', 'Visayas', 'Visayas', 'Visayas',
               'Mindanao', 'Mindanao', 'Mindanao', 'Mindanao',
               'Luzon', 'Luzon', 'Visayas', 'Visayas',
               'Mindanao', 'Mindanao'],
    'city': ['Manila', 'Manila', 'Baguio', 'Baguio',
             'Cebu', 'Cebu', 'Iloilo', 'Iloilo',
             'Davao', 'Davao', 'Cdo', 'Cdo',
             'Manila', 'Baguio', 'Cebu', 'Iloilo',
             'Davao', 'Cdo'],
    'year': [2021, 2022, 2021, 2022,
             2021, 2022, 2021, 2022,
             2021, 2022, 2021, 2022,
             2023, 2023, 2023, 2023,
             2023, 2023],
    'revenue': [120000, 135000, 80000, 92000,
                95000, 103000, 60000, 68000,
                75000, 82000, 45000, 51000,
                140000, 96000, 108000, 72000,
                88000, 55000]
})

pivot = sales_data.pivot_table(
    values='revenue', index=['region', 'city'],
    columns='year', aggfunc='sum'
)

"""
All rows, only years 2021 and 2022.

Rows from ('Luzon', 'Baguio') to ('Mindanao', 'Davao'), all years.

Rows from ('Luzon', 'Baguio') to ('Mindanao', 'Davao'), years 2021 to 2022.

Countries 'Luzon' through 'Mindanao', only the 2022 column.

State the shape and type of each result — DataFrame or Series — and explain why #4 returns what it returns.
"""

print(pivot)
print('------------------------------------')
print(pivot.loc[:, 2021:2022])
print('------------------------------------')
print(pivot.loc[('Luzon','Baguio'):('Mindanao','Davao')])