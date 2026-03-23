"""Handling missing Data
"""

import pandas as pd
data = {
    "Name":[None,None,"C","D","E","F","G","H","I","J","K","L"],
    "Age":[24,None,27,24,23,29,35,35,37,38,49,55],
    "Income":[50000,None,150000,200000,150000,250000,500000,350000,500000,500000,9000000,10000000],
    "Performance":[60,None,80,85,85,87,90,89,90,90,95,99]
}
df = pd.DataFrame(data)
print(df)
print()
print(df.isnull())
print(df.isnull().sum())
print()

"""df.loc[1,["Name","Age","Income","Performance"]] = "B",25,70000, 70
print(df)"""

