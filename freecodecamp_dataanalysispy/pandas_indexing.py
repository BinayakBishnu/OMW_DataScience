import pandas as pd

S = pd.Series({'ABC': 'a', 'DEF': 'b', 'GHI': 'c',
              'JKL': ['a', 'b', 'c', 'a']})

print(S)

print(S[0])
print(S.iloc[0])

print(S['DEF'])
print(S.loc['DEF'])

print(S['JKL'])
print(S.loc['JKL'])

print(S.loc[['DEF', 'JKL']])


print()
A = pd.Series([34, 65, 12, 87, 32, 74, 37])
print(A)
print(A.mean())
print(A.std())

A *= 100
# print(A)
print(A.mean())
print(A.std())

A += 20
# print(A)
print(A.mean())
print(A.std())

print(S[S > S.mean()])
