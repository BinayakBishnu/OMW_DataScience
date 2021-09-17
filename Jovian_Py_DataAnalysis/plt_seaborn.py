import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


p1 = [2000,2001,2002,2003,2004]
p2 = [2,5,1,8,8]
p3 = [7,8,1,5,1]

# plt.bar(p1,p2)
# plt.bar(p1,p3, alpha=0.5)

# plt.bar(p1,p2)
# plt.bar(p1,p3, bottom=p2)
# plt.show()

# sns.barplot(x=p1, y=p2)
# plt.show()

flight_data1 = pd.read_csv("./Airline_sample.csv", index_col="Month")
# print(flight_data)

# flight_data = flight_data1.transpose()
# plt.figure(figsize=(20,10))
# sns.heatmap(data = flight_data, annot=True,cmap="Blues")
# plt.show()

# from PIL import Image
# import numpy as np
# img = Image.open('./calculus4DS.png')
# img_arr = np.array(img)
# print(img_arr.shape)
# # print(img_arr)

# plt.grid(True)
# plt.title('Calculus for Data Science')
# plt.axis('off')
# plt.imshow(img)

# plt.imshow(img)
# plt.show()

# sns.pairplot(flight_data1)
# plt.show()

fig, axes = plt.subplots(2, 3,
figsize=(16,8),
)


sns.barplot(x=flight_data1.index, y=flight_data1['NK'], ax=axes[0,0])
sns.heatmap(data=flight_data1, ax=axes[0,1])

data_df = pd.read_csv("./Sample.csv",index_col=0,parse_dates=True)
sns.lineplot(data=data_df, ax=axes[1,0])
sns.lineplot(data=data_df['Rate'], label="Rates", ax=axes[1,1])
sns.lineplot(data=data_df['Quantity'], label="Quantity", ax=axes[1,2])

# plt.tight_layout(pad=2)
plt.show()

