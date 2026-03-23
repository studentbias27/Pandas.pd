"""sorting & Aggregation."""
#sorting

import pandas as pd
data = {
    "Name":["Ayush","Pawan","Rohit"],
    "Salary":[500000,150000,50000],
    "Age":[19,30,26]
}
df = pd.DataFrame(data)
#print(df)
#df.sort_values(by=["time","value"],ascending = [True,False], inplace=True)
#df.reset_index(drop=True,inplace=True)
df.sort_values(by=["Age","Salary"], ascending = [True,True], inplace=True)
print(df)

"""secondary key work when in primary two key are same"""

"""agg."""
avg_salary = df["Salary"].mean()
print(avg_salary)

"""like you can do many things """

