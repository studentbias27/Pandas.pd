# convert into pnadas df, add new column status, find average marks.
'''data = {
    "name": ["A","B","C","D"],
    "marks":[85,42,78,90]
}
print(data)'''

import pandas as pd
data = {
    "name": ["A","B","C","D"],
    "marks":[85,42,78,90],
    
}
df = pd.DataFrame(data)
print(df)
df["status"] = "pass"
df.loc[df["marks"] <= 50, "status"] = "fail"
print(df)

avg = df["marks"].mean()
print(avg)

