import pandas as pd

transactions = pd.DataFrame({
    'txn_id': ['T01', 'T02', 'T03', 'T04', 'T05', 'T06', 'T07', 'T08'],
    'customer': ['Maria', 'Juan', 'Ana', 'Pedro', 'Liza', 'Ben', 'Rico', 'Jen'],
    'amount': [1500, 2200, 800, 3100, 1750, 950, 2600, 1200],
    'method': ['GCash', 'Cash', 'GCash', 'Card', 'Cash', 'GCash', 'Card', 'Cash'],
    'status': ['Paid', 'Paid', 'Pending', 'Paid', 'Paid', 'Pending', 'Paid', 'Paid']
})

print(transactions.iloc[4, 2])     # 1750 — scalar
print(transactions.iloc[:3])       # first 3 rows, all columns
print(transactions.iloc[:, 1:4])   # all rows, customer/amount/method
print(transactions.iloc[:4, 2:4])  # first 4 rows, amount/method
#the first one is a scalar while the remaining was a dataframe because it has more than one row and column