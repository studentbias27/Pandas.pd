"""grouping"""

import pandas as pd
data = {
    "Name":["Ayush","Pawan","Rohit","Rahul"],
    "Salary":[500000,200000,150000,50000],
    "Age":[19,30,30,26]
}
df = pd.DataFrame(data)
group = df.groupby("Age")["Salary"].sum()
print(group)
group = df.groupby(["Age","Name"])["Salary"].mean()
print(group)
