"""Updating values"""
import pandas as pd
data = {
    "Name":["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age":[24,25,27,24,23,29,35,35,37,38,49,55],
    "Income":[50000,60000,150000,200000,150000,250000,500000,350000,500000,500000,9000000,10000000],
    "Performance":[60,70,80,85,85,87,90,89,90,90,95,99]
}
df = pd.DataFrame(data)
print(df)

df.loc[2, "Income"] = 220000
print(df)

df.loc[[4,7], "Age"] = 28,36
print(df)

df.loc[7, ["Age", "Income"]] = 45,8000000
print(df)


"""removing"""
df.drop(columns=["Performance", "Age"], inplace=True)
print(df)

