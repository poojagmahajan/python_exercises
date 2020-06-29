
## Until now, only one level of indexing was mentioned for both the Series and DataFrame,
# but the indexes can also be multileveled.
# This is when one index refers to one or more indexes, and those indexes further refer to values.
# This can be useful when dealing with different kinds of data.

import numpy as np
import pandas as pd
# Declaring a multilevel indexed Series
srs = pd.Series(np.arange(5), index=[['A','A','B','B','B'],[1,2,3,4,5]])

print("The multileveled index in Series:")
print(srs)

print("\nThe A index:")
print(srs['A']) # Fetching elements at index named A

print("\nThe B index:")
print(srs['B']) # Fetching elements at index named B

## A DataFrame has multiple levels of columns as well as multiple levels of indexes.
# The following example explains this behavior.

import numpy as np
import pandas as pd
# Declaring a multilevel indexed DataFrame
df = pd.DataFrame(np.arange(25).reshape(5,5), index=[['A','A','A','B','B'], [1,2,3,4,5]],
                        columns=[['USA', 'Pak', 'Pak', 'UK','Ind'], ['Day', 'Day','Night', 'Night', 'Night']])

print("The multileveled index in DataFrame:\n")
print(df)