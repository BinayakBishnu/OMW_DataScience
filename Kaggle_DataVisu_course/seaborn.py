import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

data = pd.read_csv("./Sample.csv",index_col=0,parse_dates=True)

print(data)

# Set the width and height of the figure
plt.figure(figsize=(16,6))

sns.lineplot(data=data)
