import numpy as np
import pandas as pd
import pylab
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("Ds_in_Py_trial.csv")
data.head()

print(data.shape)
output = (11,5) 

x = data['Date']
y = data['Amazon']
plt.plot(x,y)
plt.xticks(np.array([0,4,9]), ['Apr 1','Apr 8','Apr 15'])
plt.title('Amazon stock price (in dollars) for April 2021',size=14)
plt.show()

# cols=data.columns[1:5]
# print(cols)
# output = Index(['Apple', 'Tesla', 'Google', 'Amazon'], dtype='object')
# sns.pairplot(data[cols], height=3.0)