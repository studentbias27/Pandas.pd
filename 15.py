"""Merging and concetenate"""

import pandas as pd
df_customers = pd.DataFrame({
    "customerId":[1,2,3],
    "Name":["Ramesh","Suresh","Kalpesh"]
})

df_orders = pd.DataFrame({
    "customerId":[1,2,4],
    "Order":[250,450,350]
})

df_merge = pd.merge(df_customers, df_orders, on="customerId",  how="outer")
print("outer join")
print(df_merge)
"""inner, outer, left, right, croos - No on= """""
