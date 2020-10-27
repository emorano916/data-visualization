import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import Counter
from operator import itemgetter
#===================================================
plt.style.use('fivethirtyeight')
with open('amazon_co-ecommerce_sample.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    list_of_manufacturers = []
    for line in csv_reader:
        list_of_manufacturers.append(line[2])
    counting_manu = Counter(list_of_manufacturers).most_common(5)


names_of_manufacturers = []
most_products = []
for i in counting_manu:
    names_of_manufacturers.append(i[0])
    most_products.append(i[1])
plt.bar(names_of_manufacturers, most_products)
plt.xlabel('Popular Manufacturers')
plt.ylabel('number of products')
plt.title("Top manufacturers in 'Amazon'")
plt.show()
