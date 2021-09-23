import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# #! date
# today = datetime.date.today()
# print("Today's date:", today)

# # dd/mm/YY
# d1 = today.strftime("%d/%m/%Y")
# print("d1 =", d1)

# # Textual month, day and year	
# d2 = today.strftime("%B %d, %Y")
# print("d2 =", d2)

# # mm/dd/y
# d3 = today.strftime("%m/%d/%y")
# print("d3 =", d3)

# # Month abbreviation, day and year	
# d4 = today.strftime("%b-%d-%Y")
# print("d4 =", d4)

# print("\n\n")

# #! time
# now = datetime.datetime.now()

# # datetime object containing current date and time
# now = datetime.datetime.now()
 
# print("now =", now)

# # dd/mm/YY H:M:S
# dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
# print("date and time =", dt_string)	

data_df = pd.read_csv("./landslides.csv")
# print(data_df)

data_df['parsed'] = pd.to_datetime(data_df['date'],format="%m/%d/%y")
print(data_df['parsed'])

days = data_df['parsed'].dt.day
print(days)
sns.histplot(days,kde=False, bins=31)
plt.show()

