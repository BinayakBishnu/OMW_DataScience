import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from scipy import stats
from mlxtend.preprocessing import minmax_scaling
import datetime
import chardet
# import thefuzz
# from thefuzz import process

pd.plotting.register_matplotlib_converters()
# %matplotlib inline

earthquake_data = pd.read_csv(
    'Kaggle Projects/1.earthquake_all_month.csv', index_col='id')
# print(earthquake_data)
# print(earthquake_data.head())
# print(earthquake_data.sample(8))
print(earthquake_data.info())
# * therefore need to parse date-time
# print(earthquake_data.describe())
# col_names = [column for column in earthquake_data.head()]
# print(col_names)

#! print(earthquake_data.loc[earthquake_data['nst'].isnull(),['time']])
#! print(earthquake_data.nst.dtype)
#! earthquake_data.nst = earthquake_data.nst.fillna(0.0)
#! print(earthquake_data.loc[earthquake_data['nst'].isnull(),['time']])
#!
for column in earthquake_data.head():
    # print(earthquake_data[column].dtype)
    if (earthquake_data[column].dtype) == 'float64':
        # print(earthquake_data.loc[earthquake_data[column].isnull(),['time',column]])
        earthquake_data[column] = earthquake_data[column].fillna(0.0)
        # print(earthquake_data.loc[earthquake_data[column].isnull(),['time',column]])

""" for column in earthquake_data.head():
    # print(earthquake_data[column].dtype)
    if (earthquake_data[column].dtype) == 'object':
            # print(earthquake_data.loc[earthquake_data[column].isnull(),['time',column]])
            if earthquake_data.loc[earthquake_data[column].isnull(),['time',column]].empty != 1:
                print('Column:',column)
                print(earthquake_data.loc[earthquake_data[column].isnull(),[column,'mag']]) """

# * only magType is object type column having null values
# * calculation complicated and needs values not present
# * therefore dropping them

# print(earthquake_data.loc[earthquake_data['magType'].isnull(),['magType','mag']])
indices_with_magType_null = earthquake_data.index[earthquake_data['magType'].isnull(
)].tolist()
# print(indices_with_magType_null)
earthquake_data = earthquake_data.drop(index=indices_with_magType_null)
# print(earthquake_data.loc[earthquake_data['magType'].isnull(),['magType','mag']])

""" float_type_cols = [column for column in earthquake_data.head() if earthquake_data[column].dtype == 'object']
# print(float_type_cols)
unique_values_in_float_columns = [earthquake_data[column].unique() for column in float_type_cols]

float_columns_unique_values_paired = list(zip(float_type_cols,unique_values_in_float_columns))
# print(float_columns_unique_values_paired)

for pair in float_columns_unique_values_paired:
    print(pair[0],'->',pair[1]) """
# * no inconsistency

""" print((earthquake_data['locationSource'] !=
        earthquake_data['magSource']).sum()) """
# * 5 sources not equal


# ? dmin = horizontal distance, epicenter to nearest station
# ? show relation with depth error
# sns.scatterplot(x = earthquake_data.dmin, y = earthquake_data.depthError)
# sns.regplot(x = earthquake_data.dmin, y = earthquake_data.depthError)
# plt.xlim(0,150)
# plt.ylim(0,150)
# sns.histplot(x = earthquake_data.dmin, y = earthquake_data.depthError)
# sns.barplot(x = earthquake_data['dmin'], y = earthquake_data['depthError'])
# plt.ylabel("depthError vs dmin")
# sns.lineplot(data=earthquake_data['dmin'], label="plot")
plt.show()

# ? show relation of magnitude with depth
