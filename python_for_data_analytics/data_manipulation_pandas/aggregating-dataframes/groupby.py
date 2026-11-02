import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'region': ['Luzon', 'Visayas', 'Mindanao', 'Luzon', 'Visayas', 'Mindanao',
               'Luzon', 'Visayas', 'Mindanao', 'Luzon', 'Visayas', 'Mindanao'],
    'channel': ['Online', 'Online', 'Online', 'In-store', 'In-store', 'In-store',
                'Online', 'Online', 'Online', 'In-store', 'In-store', 'In-store'],
    'order_value': [5200, 3100, 2400, 6800, 4500, 3300,
                    7100, 3900, 2800, 8400, 5100, 3600]
})


    #Group orders by region, sum order_value, save as sales_by_region. Print it.
    #Compute the proportion of sales per region, save as propn_by_region. Print it.
    #Group orders by region and channel, sum order_value, save as sales_by_region_channel. Print it.
    #In one sentence: how many rows does sales_by_region_channel have, and why?

sales_by_region = orders.groupby('region')['order_value'].sum()
propn_by_region = sales_by_region / sales_by_region.sum()
sales_by_region_channel = orders.groupby(['region','channel'])['order_value'].sum()
print(sales_by_region)
print("-----------------")
print(propn_by_region)
print("-----------------")
print(sales_by_region_channel)

#it has 6 columns since in the channels it has 2 (in-store and online). although we have a groupby, 
# but the first groupby (the region) will be the first to be executed