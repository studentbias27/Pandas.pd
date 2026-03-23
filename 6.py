"""1- select specific  - 
2- filter rows
3- combine multiple conditions"""

import pandas as pd

data = {
    "Name":["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age":[19,20,21,22,23,24,25,26,27,28,29,30],
    "Income":[50000,60000,150000,200000,150000,250000,500000,350000,500000,500000,1000000,10000000],
    "Performance":[60,70,80,85,85,87,90,89,90,90,95,99]
}
df = pd.DataFrame(data)

#1-selecting column
column = df['Age']
#subset = df[['Age','Income']]
print(column)
#print(subset)
print()

#2- filtering rows--
filter_rows = df[df['Age']> 21]
print(filter_rows)
print()

#3 - combining multiple conditions-

specific = df[(df['Age'] >21) & (df['Age'] < 26)]
print(specific)
print()

specific1 = df[(df['Age'] >21) & (df['Performance'] > 70)]
print(specific1)
print()

specific2 = df[(df['Age'] >26) | (df['Performance'] > 70)]
print(specific2)
