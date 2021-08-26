import pandas as pd

""" data = pd.read_csv("./business-financial-data-mar-2021-quarter-csv.csv")

print(data.shape)

print(data.head()) """


data = pd.read_csv("./business-financial-data-mar-2021-quarter-csv.csv",index_col=0)

# print(data.head())

""" print(data.Period)
print(data['Period'])   #* same
print(data['Period'][1]) """

""" print(data.iloc[0]) # first row
print(data.iloc[:,1])   # 2nd column
print(data.iloc[:3,0])  # 1st column for first 3 rows
print(data.iloc[5:20,0])  # 1st column for 6th to 20th rows
print(data.iloc[[3,9,17],0])  # 1st column for 6th to 20th rows
print(data.iloc[-9:,0])  # 1st column for 6th to 20th rows """

print(data.loc['BDCQ.SF1AA2CA','Data_value'])
print(data.loc[:,'Data_value'])
