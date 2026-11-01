import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_id': ['C1', 'C1', 'C2', 'C3', 'C2', 'C4', 'C3', 'C1', 'C5', 'C2'],
    'city': ['Manila', 'Cebu', 'Manila', 'Davao', 'Cebu', 'Manila', 'Manila', 'Davao', 'Cebu', 'Manila'],
    'payment_method': ['GCash', 'Cash', 'GCash', 'Credit Card', 'GCash', 'Cash', 'GCash', 'Credit Card', 'Cash', 'GCash']
})

#Count the number of orders per city. Save as city_counts and print.
#Count the proportion of orders per city. Save as city_props and print.
#Count the number of orders per payment_method, sorted descending. Save as payment_counts and print.
#Count the proportion of orders per payment_method. Save as payment_props and print.
#In one sentence: what does a proportion tell you that a raw count doesn't?

city_counts = orders['city'].value_counts()
print(city_counts)
city_props = orders['city'].value_counts(normalize=True)
print(city_props)
payment_counts = orders['payment_method'].value_counts(ascending=False)
print(payment_counts)
payment_props = orders['payment_method'].value_counts(normalize=True)
print(payment_props)
#so basically an .value_counts() counts how many reoccuring values in a field
#proportion(normalize=True) is fraction of the whole like how many percent is that of the total