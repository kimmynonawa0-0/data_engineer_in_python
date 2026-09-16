import matplotlib.pyplot as plt

temps = [22, 24, 25, 23, 26, 27, 28, 30, 31, 29,
         26, 25, 24, 23, 22, 21, 20, 19, 18, 17,
         19, 21, 23, 25, 27, 29, 30, 32, 31, 28]

plt.hist(temps, bins=15, edgecolor='black')
plt.show()
