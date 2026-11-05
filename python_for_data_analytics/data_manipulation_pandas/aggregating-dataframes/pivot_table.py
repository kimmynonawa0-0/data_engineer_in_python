import pandas as pd

orders = pd.DataFrame({
    'region': ['Luzon', 'Luzon', 'Luzon', 'Luzon',
               'Visayas', 'Visayas', 'Visayas', 'Visayas',
               'Mindanao', 'Mindanao', 'Mindanao', 'Mindanao'],
    'channel': ['Online', 'Online', 'In-store', 'In-store',
                'Online', 'Online', 'In-store', 'In-store',
                'Online', 'Online', 'In-store', 'In-store'],
    'order_value': [5200, 7100, 6800, 8400,
                    3100, 3900, 4500, 5100,
                    2400, 2800, 3300, 3600]
})


"""
	Use .pivot_table() to get the mean and sum of order_value by region. Save as region_pivot and print.

	Use .pivot_table() to get the mean of order_value with region as rows and channel as columns. Save as region_channel_pivot and print.

	State the shape of each output.

	In one sentence: which of these two would you use for a report, and why?
"""
region_pivot = orders.pivot_table(values='order_value',index='region', aggfunc=['mean','sum'])
print(region_pivot)
region_channel_pivot = orders.pivot_table(values='order_value',index='region',columns='channel')
print(region_channel_pivot)
#i would use the second one because it has a column, by that it is more detailed to know if its online or in store of the order value