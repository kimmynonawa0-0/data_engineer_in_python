import pandas as pd
import matplotlib.pyplot as plt

delivery_times = pd.DataFrame({
    'order_id': list(range(1, 21)),
    'courier': ['Express', 'Express', 'Express', 'Express', 'Express',
                'Express', 'Express', 'Express', 'Express', 'Express',
                'Standard', 'Standard', 'Standard', 'Standard', 'Standard',
                'Standard', 'Standard', 'Standard', 'Standard', 'Standard'],
    'minutes': [25, 28, 30, 32, 35, 38, 40, 42, 45, 48,
                45, 50, 55, 58, 60, 65, 68, 72, 75, 80]
})

"""
Create a histogram of minutes for Express couriers, with alpha=0.5 and bins=10.

Create a histogram of minutes for Standard couriers, on the same plot, with alpha=0.5 and bins=10.

Add a legend using the label= parameter in each hist() call, then a bare plt.legend().

Add a title 'Delivery Time Distribution: Express vs Standard' and x-label 'Minutes'.

Show the plot.

In one sentence: why does alpha=0.5 matter for this comparison specifically?

"""

delivery_times[delivery_times['courier']=='Express']['minutes'].hist(
    alpha=0.5, 
    bins=10,
    label='Express'
    )
delivery_times[delivery_times['courier']== 'Standard']['minutes'].hist(
    alpha= 0.5,
    bins= 10,
    label='Standard'
)
plt.legend()
plt.title('Delivery Time Distribution: Express vs Standard')
plt.xlabel('Minutes')
plt.ylabel('Frequency')
plt.show()