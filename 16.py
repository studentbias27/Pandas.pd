"""concetenate - combinong vertically and horizently"""
import pandas as pd
df_data1 = pd.DataFrame({
    "customerId":[1,2,3],
    "Name":["Ramesh","Suresh","Kalpesh"]
})

df_data2 = pd.DataFrame({
    "customerId":[4,5],
    "Name":["Ramu","SurDa"]
})
#horix]zontal in vertical axis = 0
df_concat = pd.concat([df_data1,df_data2], axis=0, ignore_index = True)
print(df_concat)
