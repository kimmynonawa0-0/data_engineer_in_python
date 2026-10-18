import pandas as pd

countries = pd.DataFrame({
    'country': ['Philippines', 'Japan', 'Singapore', 'Malaysia', 'Thailand',
                'Vietnam', 'Indonesia', 'South Korea', 'Hong Kong', 'Taiwan'],
    'population': [110000000, 125000000, 5700000, 33000000, 70000000,
                   98000000, 275000000, 51000000, 7500000, 23500000],
    'internet_users': [73000000, 115000000, 5500000, 29000000, 55000000,
                       70000000, 185000000, 49000000, 7200000, 21000000]
})

"""
    Add a column internet_pct = percentage of the population that uses the internet. Formula: 100 * internet_users / population.
    Filter for countries where internet_pct > 80. Save as high_internet.
    Sort high_internet by descending internet_pct. Save as high_internet_srt.
    Select only country and internet_pct columns. Save as result.
    Print result.
"""

countries['internet_pct'] = 100 * countries['internet_users'] / countries['population']
countries['high_internet'] = countries['internet_pct']>80
high_internet_srt = countries.sort_values('high_internet',ascending=False)
result = high_internet_srt[['country','internet_pct']]
print(result)