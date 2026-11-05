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
                    2400, 2800, 3300, 3600],
    'delivery_days': [2, 3, 4, 1,
                      5, 2, 3, 6,
                      4, 2, 5, 3]
})

#Group by region, aggregate order_value with min, max, mean, median (in that order). Save as region_stats, print.
#Group by region and channel, aggregate order_value and delivery_days with mean and sum (in that order). Save as region_channel_stats, print.
#State the shape of each output and explain why the second one's columns are a MultiIndex.



region_stats = orders.groupby('region')['order_value'].agg(['min','max','mean','median'])
print(region_stats)
region_channel_stats = orders.groupby(['region','channel'])[['order_value','delivery_days']].agg(['mean','sum'])
print(region_channel_stats)
#i can only think of because each field has its mean and sum so thats why they are multi index?