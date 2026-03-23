"""save data into files"""
import pandas as pd

data = {
    "name":["Ayush", "Harsh", "Deepak", "Harshit"],
    "Age": [19,21,22,19],   
}

df = pd.DataFrame(data)
print(df)

#df.to_csv("a.csv", index=False) # index=False for removing unneccecary indexing.
#df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)
