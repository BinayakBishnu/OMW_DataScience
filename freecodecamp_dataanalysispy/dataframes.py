import pandas as pd

A = pd.DataFrame({
    'Population': [34, 54, 23],
    'Status': ['AB', 'FQ', 'JL'],
    'Growth': [3, 6, 1],
}, columns=['Population', 'Status', 'Growth'])
A.index = ['North', 'West', 'South']
print(A)

A['Deaths'] = 0
print(A)

births = pd.Series([10, 9], index=['North', 'South'])
A['Births'] = births
print(A)
