
# sum(axis=0) : This function calculates the sum of each column of a DataFrame.
# sum(axis=1) : This function calculates the sum of each row of a DataFrame.
# min(axis=0) : This function returns the minimum value from each column.
# min(axis=1) : This function returns the minimum value from each row.
# idxmin(axis=0) : This function returns the index with minimum value from every column.
# idxmin(axis=1) : This function returns the column with minimum value from every index.

import numpy as np
import pandas as pd
# Declaring DataFrame
df = pd.DataFrame(np.arange(9).reshape(3,3), index=['A', 'B', 'C'], columns=['A', 'B', 'C'])

print("The DataFrame")
print(df)

print("\nThe sum of each Column:")
print(df.sum(axis=0))

print("\nThe sum of each Row:")
print(df.sum(axis=1))

print("\nThe minimum from each Column:")
print(df.min(axis=0))

print("\nThe minimum from each Row:")
print(df.min(axis=1))


print("\nThe minimum value in each Column is at index:")
print(df.idxmin(axis=0))

print("\nThe minimum value at each index is at Column:")
print(df.idxmin(axis=1))