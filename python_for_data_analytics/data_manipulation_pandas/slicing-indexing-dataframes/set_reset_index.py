import pandas as pd

stores = pd.DataFrame({
    'store_id': ['S01', 'S02', 'S03', 'S04', 'S05'],
    'city': ['Manila', 'Cebu', 'Davao', 'Manila', 'Baguio'],
    'monthly_sales': [450000, 320000, 280000, 510000, 190000],
    'employees': [12, 8, 7, 15, 5]
})

"""
Set store_id as the index, saving as stores_ind. Print.

Print stores_ind reset with the index contents kept as a column.

Print stores_ind reset with the index contents dropped.

In one sentence: after step 3, what happened to the store_id values, and can you recover them from that DataFrame?

How many columns does stores_ind have, and how many does step 3's output have?
"""

print(stores)
stores_ind = stores.set_index('store_id')
print(stores_ind)
print(stores_ind.reset_index())
print(stores_ind.reset_index(drop=True))
#the store_id was gone because it was just a field used as an index. ofc u can recover it by removing the drop=True or setting to false
#only 3. it has 4 outputs