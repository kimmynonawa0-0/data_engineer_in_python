import pandas as pd

store_performance = pd.DataFrame({
    'store': ['S01', 'S02', 'S03', 'S04', 'S05', 'S06'],
    'region': ['Luzon', 'Visayas', 'Mindanao', 'Luzon', 'Visayas', 'Mindanao'],
    'revenue_per_sqft': [1250, 980, 870, 1420, 1050, 920],
    'monthly_revenue': [450000, 320000, 280000, 510000, 380000, 310000]
})

"""
Sort store_performance by revenue_per_sqft from highest to lowest. Save as top_stores and print it.

Save top_stores as "top_stores.csv" using default settings — no index=False.

Open the file in VSCode and look at the first column. Note what's in it.

Save the same DataFrame again as "top_stores_clean.csv" with index=False.

Open that file and compare it to the first one. State the difference in one sentence.

In one sentence: which of the two files would you send to a colleague, and why?
"""

# 1. Sort descending. sort_values PRESERVES the original row index,
#    so after sorting the indices are out of order: 3, 0, 4, 1, 5, 2
top_stores = store_performance.sort_values('revenue_per_sqft', ascending=False)
print(top_stores)

# 2. Save with DEFAULT settings → index=True → extra unnamed first column
#    containing the original row numbers (3, 0, 4, 1, 5, 2)
top_stores.to_csv('top_stores.csv')

# 3. In VSCode, top_stores.csv's first column = row indices (3, 0, 4, 1, 5, 2)

# 4. Save WITH index=False → no index column, starts directly with 'store'
top_stores.to_csv('top_stores_clean.csv', index=False)

# 5. Difference: top_stores.csv has an extra unnamed first column with the
#    original row indices (3, 0, 4, 1, 5, 2); top_stores_clean.csv starts
#    directly with the 'store' column.

# ── ANSWERS ─────────────────────────────────────────────────────────────
# Q3 (first column of top_stores.csv):
#   The original row indices — 3, 0, 4, 1, 5, 2 — out of order because
#   sort_values keeps the original index labels, not new 0–5 ones.
#
# Q5 (difference, one sentence):
#   top_stores.csv has an extra unnamed first column holding the original
#   row indices (3, 0, 4, 1, 5, 2), while top_stores_clean.csv starts
#   directly with the 'store' column.
#
# Q6 (which to send, one sentence):
#   Send top_stores_clean.csv (index=False) because row numbers are
#   meaningless DataFrame artifacts — and since they appear out of order
#   after sorting, they look like noise or a data error to a colleague.
