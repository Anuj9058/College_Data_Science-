import pandas as pd
import numpy as np
import seaborn as sb
import plotly.graph_objects as go



data = pd.read_csv('world-data-2023.csv')

# count = 1
# for col in data.shape:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.head:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.columns:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.describe:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.axes:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.tail(7):
#     print(f"{count}: {col}")
#     count += 1


# count = 1
# for col in data.aggregate:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.pivot_table:
#     print(f"{count}: {col}")
#     count += 1


# count = 1
# for col in data.expanding:
#     print(f"{count}: {col}")
#     count += 1
 

# count = 1
# for col in data.iloc:
#     print(f"{count}: {col}")
#     count += 1

# count = 1
# for col in data.pivot:
#     print(f"{count}: {col}")
#     count += 1


# count = 1
# for col in data.is_unique:
#     print(f"{count}: {col}")
#     count += 1

# print(data.expanding)

# print(data.pivot)

# print(data.reindex)

# print(data.pivot_table)



#USING MATPLOT LIB
import matplotlib.pyplot as plt
# x = [1,2,3,4,5]
# y = [2,4,6,8,10]

# plt.plot(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Line Graph')
# plt.show()

# categories = [10,5,7]
# values = ['A','B','C']
# plt.bar(categories,values)
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Bar Chart')
# plt.show()

# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.scatter(x,y)
# plt.xlabel('X-axis')
# plt.ylabel('Y=axis')
# plt.title('Scatter Plot')
# plt.show()

# x=[1,2,3,4,5]
# y=[2,4,6,8,10]
# plt.plot(x,y,linestyle='--',marker='o',color='red',label='Data')
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Customized line Graph')
# plt.legend()
# plt.show()


# categories = ['A','B','C']
# values1 = [10,5,7]
# values2 = [6,8,4]
# plt.bar(categories,values1,label='values1')
# plt.bar(categories,values2,label='Values2',bottom=values1)
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Stacked Bar Chart')
# plt.legend()
# plt.show()


import numpy as np
np.random.seed(42)
data= np.random.randn(1000)
plt.hist(data,bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()