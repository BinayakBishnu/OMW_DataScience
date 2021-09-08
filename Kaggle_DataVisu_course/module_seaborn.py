import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data_df = pd.read_csv("./Sample.csv",index_col=0,parse_dates=True)

print(data_df)

# Set the width and height of the figure
plt.figure(figsize=(20,6))

# plt.title('Sales')
# sns.lineplot(data=data_df)
# plt.show()


# print(list(data_df.columns))
# *printing subset of data
# sns.lineplot(data=data_df['Rate'], label="Rates")
# sns.lineplot(data=data_df['Quantity'], label="Quantity")
# plt.show()



