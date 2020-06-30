
'''Reshaping is considered a powerful tool for getting the data ready for analysis.
 It transforms the initial data model into the desired shape to ease the cleaning and manipulation of data for further analysis.
This technique is usually performed on a Series or DatFrame with multiple indexes.'''

### Stack ###

## Stacking a pandas DataFrame means taking the innermost level of column index from a multi-indexed DataFrame
# and adding it as another level to the innermost row index.
# If the DataFrame is not multi-indexed, it takes the first column and moves it to the innermost row level.

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape(3,4), index = ['Row1', 'Row2', 'Row3'],
                                            columns = ['Col1','Col2','Col3','Col4',])

df.index.name = 'Row'
df.columns.name = 'Column'

print("The Original DataFrame")
print(df,'\n')

print("The Stacked DataFrame")
print(df.stack())

### Unstack ###

## Unstacking a pandas Series or DataFrame takes the innermost level of row index from a multi-indexed DataFrame
# and adding it as another level to the innermost column indexes.
# If the DataFrame is not multi-indexed, it takes the first row and moves it to the innermost column level.

df = pd.DataFrame(np.arange(12).reshape(3,4), index = ['Row1', 'Row2', 'Row3'],
                                            columns = ['Col1','Col2','Col3','Col4',])

df.index.name = 'Row'
df.columns.name = 'Column'

print("The Original DataFrame")
print(df,'\n')

stacked_df = df.stack()
print("The Stacked DataFrame\n", stacked_df)

print("\nThe Unstacked DataFrame")
print(stacked_df.unstack(),'\n')

print("The Unstacked DataFrame on Named index")
print(stacked_df.unstack('Row'))

### Pivot Table ###

## This function creates a table that contains information from the original table based on the parameters defined by the user.
# It describes what specific information the user wants to know and how the user wants to present this information.
# The pivot function takes three parameters as row_index, column_index, value.

import numpy as np
import pandas as pd

df = pd.DataFrame({'Company': ['Google', 'Microsoft', 'Google', 'Microsoft'],
      'Product': ['Editor', 'Editor', 'Calendar', 'Azure'],
      'Price': ['$200', '$250', '$50', '$400']})

df.index.name = 'Row'
df.columns.name = 'Column'

print("The Original DataFrame")
print(df,'\n')

print("The Pivoted DataFrame")
print(df.pivot('Company', 'Product', 'Price'))