"""removing missing data in row & column if no need of them[axis = 0-row, 1= column]"""
"""filling missing data ]"""

import pandas as pd
data = {
    "Name":["A",None,"C","D","E","F","G","H","I","J","K","L"],
    "Age":[24,None,27,24,23,29,35,35,37,38,49,55],
    "Income":[500,None,1500,2000,1500,2500,5000,3500,5000,5000,9000,10000],
    "Performance":[60,None,80,85,85,87,90,89,90,90,95,99]
}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)


"""df.dropna(axis = 0, inplace=True)
print(df)df["Performance"]
print()"""

#filling default value
"""df.fillna(0, inplace=True)
print(df)
print()"""
#df= df.astype(int)
#print(df.dtypes)

#specific value-- single cloumn- [] multiple- [[]]
df[["Performance","Income","Age"]]=df[["Performance","Income","Age"]].fillna(df[["Performance","Income","Age"]].mean())

#for Row
#df.loc[1,["Age","Income","Performance"]] = 100
print(df)
df.loc[1,["Name"]] = "B"
print(df)


