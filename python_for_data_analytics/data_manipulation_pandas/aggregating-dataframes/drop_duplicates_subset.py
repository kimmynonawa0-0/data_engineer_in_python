import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'customer_id': ['C1', 'C1', 'C2', 'C3', 'C2', 'C4', 'C3', 'C1'],
    'product': ['Laptop', 'Laptop', 'Mouse', 'Keyboard', 'Mouse', 'Monitor', 'Keyboard', 'Laptop'],
    'category': ['Electronics', 'Electronics', 'Accessories', 'Accessories', 'Accessories', 'Electronics', 'Accessories', 'Electronics'],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-05'],
    'is_returned': [False, False, True, False, False, True, False, True]
})

#Remove rows with duplicate pairs of customer_id and product. Save as customer_products and print the head.
#Remove rows with duplicate pairs of product and category. Save as product_categories and print the head.
#Subset the rows where is_returned is True, then drop duplicate order_dates. Save as return_dates and print the order_date column.
#In one sentence: why does the order of "filter then dedupe" matter for Task 3?

customer_products = orders.drop_duplicates(['customer_id','product'])
print(customer_products.head())

product_categories = orders.drop_duplicates(['product','category'])
print(product_categories.head())

return_dates = orders[orders['is_returned']].drop_duplicates('order_date')
print(return_dates['order_date'])

#u must filter first so the one u will be returning has the correct rows then dropping the duplicates