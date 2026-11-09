import pandas as pd
import matplotlib.pyplot as plt

store_sales = pd.DataFrame({
    'store': ['S01', 'S01', 'S02', 'S02', 'S03', 'S03',
              'S04', 'S04', 'S05', 'S05', 'S06', 'S06'],
    'category': ['Coffee', 'Pastry', 'Coffee', 'Pastry', 'Coffee', 'Pastry',
                 'Coffee', 'Pastry', 'Coffee', 'Pastry', 'Coffee', 'Pastry'],
    'units_sold': [1200, 800, 950, 1100, 1400, 600,
                   700, 900, 1600, 1300, 850, 750],
    'region': ['Luzon', 'Luzon', 'Visayas', 'Visayas', 'Luzon', 'Luzon',
               'Mindanao', 'Mindanao', 'Luzon', 'Luzon', 'Visayas', 'Visayas']
})

"""
Print the head of store_sales.

Group by category, total units_sold, save as units_by_category, print.

Create a bar plot of total units sold by category using .plot() with explicit kind=.

Add title 'Total Units Sold by Category' and y-label 'Units Sold'.

Display the plot.

In one sentence: what would the plot look like without kind='bar', and why is that wrong?
"""

print(store_sales.head())
print('----------------------')
units_by_category = store_sales.groupby('category')['units_sold'].sum()
print(units_by_category)
print('----------------------')
units_by_category.plot(
    kind='bar',
    title='Total Units Sold by Category',
    ylabel='Units sold'
)
plt.show()
#it would return a line plot
