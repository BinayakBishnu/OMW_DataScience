import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

# data_df = pd.read_csv("./Sample.csv",index_col=0,parse_dates=True)

# print(data_df)

# Set the width and height of the figure
# plt.figure(figsize=(20,6))

# plt.title('Sales')
# sns.lineplot(data=data_df)
# plt.show()


# print(list(data_df.columns))
# *printing subset of data
# sns.lineplot(data=data_df['Rate'], label="Rates")
# sns.lineplot(data=data_df['Quantity'], label="Quantity")
# plt.show()


flight_data = pd.read_csv("./Airline_sample.csv", index_col="Month")
print(flight_data)

plt.figure(figsize=(16,6))

""" plt.title("Flight delays")
sns.barplot(x=flight_data.index, y=flight_data['NK'])
plt.ylabel("Delay (minutes)")   # always after plot
plt.show() """

plt.title("Delay Heatmap")
sns.heatmap(data=flight_data, 
annot=True) # to show numbers in cells
plt.ylabel("Month codes")   # always after plot
plt.xlabel("Flight codes")   # always after plot

plt.show()



