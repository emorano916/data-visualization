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
    amazon_category_and_sub_category = []
    for items in csv_reader:
        amazon_category_and_sub_category.append(items[8].split('>'))

category = []
counter = 0
while counter < len(amazon_category_and_sub_category):
    for z in amazon_category_and_sub_category:
        category.append(amazon_category_and_sub_category[counter][-1])
        counter+=1
Couting_each = Counter(category).most_common(5)
numb = []
catg = []
for f in Couting_each:
    numb.append(f[1])
    catg.append(f[0])
plt.bar(catg, numb)
plt.xlabel('Popular Categories')
plt.ylabel('Numbers of products')
plt.title('Top 5 categories in Amazon')
plt.show()