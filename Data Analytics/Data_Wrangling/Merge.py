
##### Merge ######

'''To merge the rows of two or more DataFrames based on a common column between them, use pandas merge(df1, df2, ...) function.
This returns another DataFrame with only the common column(s) and their corresponding row values.'''

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

print("First DataFrame")
print(df1)

df2 = pd.DataFrame({'pointer':['B', 'C', 'B','D'],
                    'value_df2':[6,7,8,9]})

print("\nSecond DataFrame")
print(df2)

print("\nMerged DataFrame")
print('\n',pd.merge(df1, df2)) # Merging two DataFrames

#### Left Merge #####

## The left merge returns a DataFrame, which has all rows of the DataFrame placed on the left side of the merge() function.
# Those rows of the left DataFrame, which do not have a corresponding matching value in the right DataFrame, are then assigned NaN values.'''

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame({'pointer':['B', 'C', 'B', 'D', 'E'],
                    'value_df2':[6, 7, 8, 9, 12]})

print("Left Merged DataFrame\n")
print(pd.merge(df1, df2, how = 'left')) # Performing a left merge
#### Right Merge ####

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame({'pointer':['B', 'Z', 'C', 'B','D','E'],
                    'value_df2':[6,7,8,9,10,11]})

print("Right Merged DataFrame\n")
print(pd.merge(df1, df2, how = 'right')) # Performing a right merge

#### Outer Merge ####

## This function returns all the rows of both the DataFrames given in the merge() function.
# The rows that don’t get matched in either case are assigned NaN values.

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame({'pointer':['B', 'Z', 'C', 'B','D','E'],
                    'value_df2':[6,7,8,9,10,11]})

print("Outer Merged DataFrame\n")
print(pd.merge(df1, df2, how = 'outer')) # Performing an outer merge

### Merge on multipe columns ####

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'column1':['Pak', 'USA', 'Pak', 'UK', 'Ind','None'], #Column 1
                    'column2':['A', 'B', 'C', 'B', 'A', 'D'],            #Column 2
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame({'column1':['USA', 'UK', 'None', 'USA', 'Pak','Ind'], #Column 1
                    'column2':['B', 'Z', 'C', 'B','D','E'],              #Column 2
                    'value_df2':[6,7,8,9,10,11]})

print("Outer Merged DataFrame on Multiple Columns\n")
print(pd.merge(df1, df2, on = ['column1', 'column2'], how = 'outer'))

### Merge on Index ###

##  The only difference is that now the column of one DataFrame is merged with the index of another DataFrame.

## For one DataFrame, the common values are changed from rows to indexes.
# Two new parameters are needed for this purpose.
# The left_on parameter that takes the column name of left DataFrame and right_index parameter that has to be set to True.

import numpy as np
import pandas as pd

df1 = pd.DataFrame({'pointer':['A', 'B', 'C', 'B', 'A', 'D'],
                    'value_df1':[0,1,2,3,4,5]})

df2 = pd.DataFrame(np.arange(10,13,1), index = ['A', 'B','C'], columns = ['values'])
print(df2)
print("Merged on index\n")
print(pd.merge(df1, df2, left_on='pointer', right_index=True))