import pandas as pd
import numpy as np

data_df = pd.read_csv("./Airline_sample.csv")

# print(data_df)
# print(data_df.head())
# print(data_df.tail())
# print(data_df.shape)

US_missing_count = data_df.US.isnull().sum()

columnwise_missing_count = data_df.isnull().sum()
print(columnwise_missing_count)

print(columnwise_missing_count[1:6])

# t = (4,5)
# print(np.product(t))

total_cells = np.product(data_df.shape)
print(total_cells)

total_missing_count = columnwise_missing_count.sum()
print(total_missing_count)
fraction_missing = total_missing_count/total_cells
print(fraction_missing*100)

"""a = 10
print("%d" %a) """




