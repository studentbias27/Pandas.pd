"""two questions
1- how big is dataset(shape)
2- names of columns  """


import pandas as pd
data = {
    "Name":["A","B","C","D","E","F","G","H","I","J","K","L"],
    "Age":[19,20,21,22,23,24,25,26,27,28,29,30],
    "Income":[50000,60000,150000,200000,150000,250000,500000,350000,500000,500000,1000000,10000000],
    "Performance":[60,70,80,85,85,87,90,89,90,90,95,99]
}

df = pd.DataFrame(data)
print(df)
print(f"shape: {df.shape}")
print(f'column name: {df.columns}')
#print("shape:", df.shape)
#print("column name:", df.columns)