import pandas as pd
df = pd.read_excel("sweetshop_data-1.xlsx")
print(df.head(3).to_string())
#print(df.info())