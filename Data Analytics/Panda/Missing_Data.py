

#dropna() : This function drops the NaN values based on several parameters that we can define in it.
#           It provides a vast range of parameters so accurate dead points in the data can be eliminated.
#           If no parameter is defined, the rows containing at least one NaN value are deleted.
#           The following are its parameterized types:

#dropna(how='all') : Deletes the rows where all values are NaN

#dropna(axis=1) : Deletes the entire column that contains at least one NaN value

#dropna(thresh=n) : Deletes the rows that contain less than n number of non NaN values

import numpy as np
import pandas as pd

null_val = np.nan

df = pd.DataFrame([['A','B','C','D'],[null_val,'B',null_val,'D'],[null_val,'B','C',null_val],[null_val,null_val,null_val,null_val]])

print("Originl DataFrame:")
print(df)
# Dropping Null values
print("\nThe dropna() method:")
print(df.dropna())

print("\nThe dropna(how = all) method:")
print(df.dropna(how = 'all'))

print("\nThe dropna(axis=1) method:")
print(df.dropna(axis=1))

print("\nThe dropna(thresh = n) method:")
print(df.dropna(thresh = 1))

# fillna(n) : This function replaces the NaN data points with our defined value n.

null_val = np.nan

df = pd.DataFrame([['A','B','C','D'],[null_val,'B',null_val,'D'],[null_val,'B','C',null_val],[null_val,null_val,null_val,null_val]])

print("Originl DataFrame:")
print(df)
# Fill the Null values
print("\nThe filled DataFrame:")
print(df.fillna('M'))