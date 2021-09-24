import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_csv("freecodecamp_dataanalysispy\sales_data.csv", parse_dates=['Date'])

# print(sales.shape)
# print(sales.head())
# print(sales.info()) #!
# print(sales.describe())
# print(sales.sample(10))

# print(sales['Unit_Cost'].describe())
# print(sales['Unit_Cost'].mean())

# sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
# sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde

# ax = sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde
# ax.axvline(sales['Unit_Cost'].mean(), color='red')
# ax.axvline(sales['Unit_Cost'].median(), color='green')

# bx = sales['Unit_Cost'].plot(kind="hist", figsize=(14,6))
# bx.set_xlabel("x values")
# bx.set_ylabel("y values")

# correlation = sales.corr()
# print(correlation)
# sns.heatmap(correlation, cmap="hot")






plt.show()

