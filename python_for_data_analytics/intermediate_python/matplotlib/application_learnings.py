import numpy as np
import matplotlib.pyplot as plt

names = ['miko','shai','serjay']
pwd = {
    'miko':'okims12',
    'shai':'shailangmalakas',
    'serjay': 'kantotmokodaddy'
}
value = [pwd[n] for n in names]
print(f"passwords are: {value}")
for p in value:
    print(p)

#task to solve from deepseek

stores = ['Store A', 'Store B', 'Store C', 'Store D', 'Store E',
          'Store F', 'Store G', 'Store H', 'Store I', 'Store J']

monthly_revenue = [45000, 38000, 52000, 28000, 61000,
                   33000, 49000, 55000, 41000, 36000]

customer_satisfaction = [4.2, 3.8, 4.7, 3.5, 4.9,
                         3.9, 4.5, 4.8, 4.1, 3.7]

num_employees = [3, 2, 4, 1, 5, 2, 3, 4, 3, 2]

region = ['Luzon', 'Visayas', 'Mindanao', 'Luzon', 'Visayas',
          'Mindanao', 'Luzon', 'Visayas', 'Mindanao', 'Luzon']
region_colors = {
    'Luzon':'red',
    'Visayas':'green',
    'Mindanao':'blue'
}
col = [region_colors[c] for c in region]
np_emp = np.array(num_employees)
np_emp = np_emp * 50
plt.scatter(monthly_revenue,customer_satisfaction, c=col, s=np_emp, alpha=0.7)
plt.xlabel('Monthly Revenue (PHP)')
plt.ylabel('Customer Satisfaction (1–5)')
plt.title('Sari-Sari Store Performance by Region')
tick_val = [30000, 40000, 50000, 60000]
tick_labels = ['30k', '40k', '50k', '60k']
plt.xticks(tick_val,tick_labels)
plt.text(61000, 4.9, 'Store E')
plt.text(28000, 3.5, 'Store D')
plt.text(52000, 4.7,'Store C')
plt.grid(True,linestyle='--',alpha=0.5)
plt.show()