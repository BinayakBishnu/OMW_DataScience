import pandas as pd

nationality = pd.Series([
    'India',
    'UK',
    'USA',
    'USA',
    'India',
    'Germany',
],
    index=[
    'ABC',
    'DEF',
    'GHI',
    'JKL',
    'MNO',
    'PQR',
]
)

print(nationality)

print(nationality.duplicated())
# print(nationality.duplicated(keep='last'))
# print(nationality.duplicated(keep=False))
# print(nationality.drop_duplicates(keep=False))
print(nationality.drop_duplicates())
# print(nationality.drop_duplicates(keep='last'))
