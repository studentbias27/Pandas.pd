"""H.W"""

import pandas as pd
data1 = pd.DataFrame({
    "customerId":[1,2,3],
    "name":["a","b","c"]
})

data2 = pd.DataFrame({
    "customerId":[4],
    "name":["d"]
})

"""df_merge = pd.merge(data1, data2, on = "customerId", how = "left" )
print("left join")
print(df_merge)"""

df_concat = pd.concat([data1,data2], axis = 0, ignore_index = True)
print(df_concat)