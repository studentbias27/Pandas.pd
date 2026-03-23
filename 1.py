""""reading data from a file and load it into a dataframe."""

import pandas as pd

# read data from CSv file into a dataframe which is provided by pandas lib.
df = pd.read_csv('data.CSv') # easy and plain text and used for single sheet
print(df)
#df = pd.read_excel('read.excel') # for binary format or multiple sheets

# used for json-
import json
data = {"Name":["Ayush", "Bob"], "Age":[19,20]}
with open('data.json', 'w') as f:
    json.dump(data,f)

df1 = pd.read_json('data.json') # plain but structured . best for APIs and web application.
# json not used for spreadsheet(matrix ) like excel and csv(less use for spredsheet)
print(df1)


""" if error use utf-8 orlatin1
if file is from cloud use gcsfs"""

