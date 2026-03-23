"""Exploring data or understanding how to understand or sumarize data."""
"""
1- understand the data set
2- identify the problems
3- plan next steps """

# 1- to see row - head and tail. int not float
import pandas as pd
df = pd.read_json("output.json")
print("Display 2 row of first")
print(df.head(2))  # () = default 5

print("Display 2 row of last")
print(df.tail(2))

# data sumary and understanding
print("displaying the info of data set")
print(df.info())
