"""DataFrame Modification---
adding column, specific value, remove unwanted."""

import pandas as pd
data = {
    "Name":["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age":[24,25,27,24,23,29,35,35,37,38,49,55],
    "Income":[50000,60000,150000,200000,150000,250000,500000,350000,500000,500000,9000000,10000000],
    "Performance":[60,70,80,85,85,87,90,89,90,90,95,99]
}

df = pd.DataFrame(data)
print(df)
# adding column through assignment - a straight forward way
df["bonus"] = df["Income"] * 0.1
print(df)

df["Married_Status"] = df["Age"] > 28
print(df)


"""2- by insert mainly used - df.inset(location, "name", data)"""

df.insert(1, "Id", [12,11,10,9,8,7,6,5,4,3,2,1])
print(df)
df.insert(5, "experience", [1,2,4,5,6,6,8,7,7,8,15,20])
print(df)
