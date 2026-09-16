import matplotlib.pyplot as plt
import numpy as np
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
visitors = [230, 450, 780, 560, 910, 1200, 880]

plt.plot(days,visitors)
plt.xlabel('day of the week')
plt.ylabel('number of visitors')
plt.title('weekly overview')
plt.clf()

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
users = [12000, 15000, 18000, 22000, 25000, 30000, 27000]
plt.plot(days, users)
plt.xlabel('day')
plt.ylabel('active sessions')
plt.title('daily active users')
tick_val = [0,12000,15000, 18000, 22000, 25000, 30000, 27000]
tick_labels = ['0','12k','15k','18k','22k','25k','30k','27k']
plt.yticks(tick_val,tick_labels)
plt.clf()
population = [1.2, 5.6, 12.3, 0.8, 8.4, 3.1]
gdp_per_capita = [35000, 18000, 12000, 42000, 9500, 22000]
happiness = [7.2, 6.1, 5.4, 7.8, 4.9, 6.6]

np_pop = np.array(population) * 3

plt.scatter(gdp_per_capita, happiness, s=np_pop)
plt.xlabel('GDP per Capita (USD)')
plt.ylabel('Happiness Index')
plt.title('City Happiness vs GDP (bubble size = population)')
plt.clf()


import matplotlib.pyplot as plt

price = [100, 250, 400, 150, 300, 500, 200, 350]
rating = [3.5, 4.2, 4.8, 3.8, 4.5, 4.9, 4.0, 4.6]
category = ['Electronics', 'Clothing', 'Electronics', 'Food',
            'Clothing', 'Electronics', 'Food', 'Clothing']

category_colors = {
    'Electronics': 'blue',
    'Clothing': 'green',
    'Food': 'orange'
}

col = [category_colors[c] for c in category]

plt.scatter(price, rating, c=col, alpha=0.7)
plt.xlabel('Price (PHP)')
plt.ylabel('Rating')
plt.title('Product Rating vs Price by Category')
plt.clf()


import matplotlib.pyplot as plt
import numpy as np

ad_spend = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
revenue = [8000, 15000, 22000, 28000, 35000, 42000, 48000, 55000]
units = [500, 800, 1200, 1600, 2000, 2400, 2800, 3200]

np_units = np.array(units)

plt.scatter(ad_spend, revenue, s=np_units, alpha=0.7, c='steelblue')
plt.xlabel('Ad Spend (PHP)')
plt.ylabel('Revenue (PHP)')
plt.title('Ad Spend vs Revenue (bubble size = units sold)')

plt.text(7000, 48000, 'Product G', fontsize=10, color='darkred')
plt.text(8000, 55000, 'Product H', fontsize=10, color='darkred')

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()