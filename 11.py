"""Interpolation-- filling astimation(pattern based) value - math based
linear , polynomial, time
1-preserve data integrity
2-smooth trands
3- avoid data loss

use- time series data
numeric data with trends
avoid droping rows.

cons- not used for str.
it's only predict not might be correct

Interpolate()"""

import pandas as pd
data = {
    "Name":["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age":[24,None,27,24,23,29,35,35,37,38,49,55],
    "Income":[500,None,1500,2000,1500,2500,5000,3500,5000,5000,9000,10000],
    "Performance":[60,None,80,85,85,87,90,89,90,90,95,99]
}
df = pd.DataFrame(data)
# = df.astype(int)
print(df)
print()

df["Age"] = df["Age"].interpolate(mathod="linear")
print(df)




