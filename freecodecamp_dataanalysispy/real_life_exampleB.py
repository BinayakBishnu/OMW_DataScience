import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_csv("freecodecamp_dataanalysispy\sales_data.csv", parse_dates=['Date'])

sales['cc'] = sales['Cost']
print(sales[['Cost','cc']].head())
sales.loc[3,'cc'] = 600
print(sales[['Cost','cc']].head())

print((sales['cc']!=sales['Cost']).sum())   #! number of different values