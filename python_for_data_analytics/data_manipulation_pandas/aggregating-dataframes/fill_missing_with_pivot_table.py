import pandas as pd

orders = pd.DataFrame({
    'region': ['Luzon', 'Luzon', 'Luzon',
               'Visayas', 'Visayas',
               'Mindanao'],
    'channel': ['Online', 'In-store', 'Online',
                'Online', 'In-store',
                'Online'],
    'order_value': [5200, 6800, 7100,
                    3100, 4500,
                    2400]
})

"""
Print the mean order_value by region (rows) and channel (columns), filling empty cells with 0.

Print the same pivot with fill_value=0 and margins=True, with the margins row/column labeled 'Total'.

State which cell would have been NaN without fill_value, and what that 0 means in plain language.

In one sentence: why does the Total row not equal the average of the printed cell values in the Mindanao column?
"""
print(orders.pivot_table(values='order_value',index='region',columns='channel',fill_value=0))
print(orders.pivot_table(values='order_value',index='region',columns='channel',fill_value=0,margins=True))
#the cell of mindanao in the in-store field. 0 means no value
#i dont know