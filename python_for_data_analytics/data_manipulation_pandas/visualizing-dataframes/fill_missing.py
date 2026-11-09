import pandas as pd
import matplotlib.pyplot as plt

inventory = pd.DataFrame({
    'store': ['S01', 'S02', 'S03', 'S04', 'S05', 'S06', 'S07', 'S08'],
    'widgets_sold': [120, None, 95, 140, None, 110, 130, 105],
    'gadgets_sold': [80, 95, None, 120, 88, None, 100, 92],
    'doohickeys_sold': [45, 60, 55, None, 70, 65, 58, 50],
    'returns': [3, 5, 2, 8, 4, 6, 3, 7]
})
"""
Create a list cols_with_missing containing the columns that have missing values (identify them first with .isna().any()).

Create a histogram of inventory[cols_with_missing]. Show the plot.

Replace missing values in inventory with 0, save as inventory_filled.

Create a histogram of inventory_filled[cols_with_missing]. Show the plot.

In one sentence: what visible change appears in the histograms after filling, and what assumption does filling with 0 make?
"""
print(inventory.isna().any())
cols_with_missing = ['widgets_sold', 'gadgets_sold', 'doohickeys_sold']
inventory[cols_with_missing].hist()
plt.show()
inventory_filled = inventory.fillna(0)
plt.clf()

inventory_filled[cols_with_missing].hist()
plt.show()

# ANSWER: visible change + assumption of fillna(0) 
# AFTER FILLING:
#   Each histogram gains a NEW SPIKE AT 0 — a bar at x=0 whose height
#   equals the number of missing values in that column
#   (widgets_sold: 2, gadgets_sold: 2, doohickeys_sold: 1).
#   The rest of the distribution's shape is unchanged; it just
#   stretches to include a new 0 bin.
#
# ASSUMPTION OF fillna(0):
#   It assumes missing = "sold zero units" (a real, observed 0).
#   That's often FALSE — missing usually means "unrecorded/unknown",
#   not "zero". Filling with 0 silently pulls the average down and
#   creates a fake "many stores sold nothing" pattern that may not
#   exist in reality.