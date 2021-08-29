import pandas as pd

""" data = pd.read_csv("./Sample.csv")

print(data.shape)

print(data.head()) """


data = pd.read_csv("./Sample.csv",index_col=0)

# print(data.head())

""" print(data.Quantity)
print(data['Quantity'])   #* same
print(data['Quantity'][1]) """

# print(data.iloc[0]) # heading with first row of values
# print(data.iloc[:,1])   # 2nd column
# print(data.iloc[:3,3])  # 4th column for first 3 rows
# print(data.iloc[5:9,2])  # 3rd column for 6th to 9th rows (excludes 9 index(10th row))
# print(data.iloc[[3,8],1])  # 4th and 9th row, second column
# print(data.iloc[-5:,0])  # 1st column for last 5

""" print(data.loc['HH6','Origin'])
print(data.loc[:,'Quality'])
print(data.loc['HH6',:]) """

# print(data[data.Quality == 'P'])

""" print(data.set_index('Quality'))
print(data) """

# print(data.loc['HH6',:])
# data.loc['MNO',:] #! error since MNO not in index col

# print(data[data.Name == 'MNO']) #? wherever MNO is Name
# print(data.loc[data.Name == 'MNO']) #? same

# print(data.loc[data.Name == 'MNO','Origin']) #? same but only Origin col

#! SUMMARIZING DATA

# print(data.Quantity.describe())
# print(data.Quantity.mean())
# print(data.Name.describe())
# print(data.Name.unique())
# print(data.Name.value_counts())

# quantity_mean = data.Quantity.mean()
# print(data.Quantity.map(lambda q: q - quantity_mean))
"""def m(q): 
    return q-quantity_mean

print(data.Quantity.map(m(q))) """

#* to plot whole table with the mapped values
#? that is, return new DataFrame and not only Series
""" quantity_mean = data.Quantity.mean()
def mean_deviation(row):
    row.Quantity = row.Quantity - quantity_mean
    return row

print(data.apply(mean_deviation,axis='columns')) """

#! neither map nor apply modify values

# quantity_mean = data.Quantity.mean()
# print(data.Quantity - quantity_mean)

# print(data.head())
# print(data.head(1))

# print(data.Name+'-'+data.Quality)

#! faster than map because they use built-in speeds up in pandas but less flexible

""" ## 6.
There are only so many words you can use
when describing a bottle of wine. Is a 
wine more likely to be "tropical" or 
"fruity"? Create a Series 
`descriptor_counts` counting how many 
times each of these two words appears in 
the `description` column in the dataset. 
"""

""" def presentornot_tropical(row):
    if 'tropical' in row.description:
        return True
    return False

tropical_bool = reviews.apply(presentornot_tropical,axis='columns')
tropical_count = 0
for i in tropical_bool:
    if i:
        tropical_count+=1

def presentornot_fruity(row):
    if 'fruity' in row.description:
        return True
    return False

fruity_bool = reviews.apply(presentornot_fruity,axis='columns')
fruity_count = 0
for i in fruity_bool:
    if i:
        fruity_count+=1

descriptor_counts = pd.Series([tropical_count,fruity_count],index=['tropical','fruity'])

# Check your answer
q6.check()
print(descriptor_counts) """

#!!
""" n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity']) """

# print(data.groupby('Origin').Origin.count())
# print(data.Origin.value_counts())

# print(data.groupby('Origin').Rate.min())

# print(data.groupby('Origin').Rate.mean())

# print(data.groupby(['Origin','Quality']).Name.unique())

# print(data.groupby(['Origin','Quality']).apply(lambda row: row.loc[row.Rating.idxmax()]))
#^ here the rows are the groups based on Origin and Quality
#^ rows are then manipulated to find max in each row

# print(data.groupby('Name').Rate.agg([len,min,max]))
# print(data.groupby('Origin').Rate.agg([len,min,max]))



