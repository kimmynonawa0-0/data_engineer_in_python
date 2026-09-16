import matplotlib.pyplot as plt

ad_spend = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
sales = [1200, 1500, 1800, 2100, 2400, 2700, 3000, 3300, 3600, 3900]

plt.scatter(ad_spend,sales)
plt.xscale('log') #logarithmic scales help visualize data with wide ranges.
plt.show()