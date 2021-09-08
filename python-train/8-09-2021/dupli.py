import pandas as pd
import numpy as np
df = pd.read_csv('employees.csv')
print(df.shape)
print(df["FIRST_NAME"].nunique())
print(df[df["FIRST_NAME"].duplicated()])
# sorting by first name
df.sort_values("FIRST_NAME", inplace = True)
 
# dropping ALL duplicate values
df.drop_duplicates(subset ="FIRST_NAME",keep = False, inplace = True)

print(df.shape)

print(df["FIRST_NAME"].nunique())

df.to_csv("duplicate_drop.csv")