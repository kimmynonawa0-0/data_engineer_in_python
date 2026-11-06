import pandas as pd

cities_data = pd.DataFrame({
    'city': ['Manila', 'Cebu', 'Davao', 'Baguio', 'Iloilo', 'Zamboanga'],
    'island_group': ['Luzon', 'Visayas', 'Mindanao', 'Luzon', 'Visayas', 'Mindanao'],
    'population_m': [1.8, 1.0, 1.8, 0.4, 0.5, 0.9]
})

"""
Create a list cities_filter containing 'Manila', 'Davao', and 'Baguio'.

Use [] with .isin() to filter cities_data for rows where city is in cities_filter. Print the result.

Set city as the index of cities_data, saving as cities_ind.

Use .loc[] to filter cities_ind for rows where the city is in cities_filter. Print the result.

In one sentence: the two filtered outputs should be identical — why does .loc[] need only the list while [] needs .isin()?
"""
cities_filter = ['Manila','Davao','Baguio']
print(cities_data[cities_data['city'].isin(cities_filter)])
cities_ind = cities_data.set_index('city')
print(cities_ind)
print(cities_ind.loc[cities_filter]) #so .loc is like subsetting pero much faster and doesnt return series of True/False
#uhm because it returns as series first then the [] wrapper makes it a dataframe 
#while the .loc doesnt need the .isin it gets the list directly since it interprets the list as labels

cities_subset = cities_data.set_index('city')
print('-------------------------------------------------------')
print(cities_subset.loc['Manila':'Zamboanga'])
print('-------------------------------------------------------')
print(cities_data.groupby('island_group')['population_m'].agg('sum'))











