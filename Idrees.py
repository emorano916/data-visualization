import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

amazon = pd.read_csv('amazon_co-ecommerce_sample.csv')
df = pd.DataFrame(amazon)
#print(df['price'].head(30))
#manufacture = df.groupby('manufacturer').sum()
#print(manufacture)
plt.style.use('fivethirtyeight')
age_x = [24, 26, 27, 28, 31, 32, 33, 44,41]
dev_y = [24000,25000,13000,31000,32100,50000,30000,50000,20000]
plt.plot(sorted(age_x), sorted(dev_y), label='Age')
plt.xlabel('Price')
plt.ylabel("Sales rate")
plt.title('Spending based on age')
plt.legend()
plt.show()
