
## Series

import numpy as np
import pandas as pd

srs = pd.Series(['A','B','C','D','D','C','A','B'])

print("Original series:")
print(srs, '\n')

print("Single value changed in Series:")
print(srs.replace('A', np.nan), '\n')

print("Multiple values changed in Series:")
print(srs.replace(['A','C'], [1, 3]))

# Dataframe

import numpy as np
import pandas as pd

df = pd. read_csv('real_estate.csv')

print("Single value changed in DataFrame:")
df = df.replace("SACRAMENTO", "Changed SACRAMENTO")
print(df.head(), '\n')

print("Multiple values changed in DataFrame:")
df = df.replace(["Changed SACRAMENTO",'CA'], ["New SACRAMENTO","AC"])
print(df.head())

