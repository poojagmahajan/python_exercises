
## We have to implement the function Sum_Swap(df).
# The df is the DataFrame on which operations will be performed.
# The task is to create a new column and a new row and then swap their values.
# The following steps are performed to calculate the values for the new row and column before swapping:

#The sum of the minimum and maximum values of each row are calculated.

#These values are assigned to the new column row_sum.

#The sum of the minimum and maximum value of each column are calculated.

#These values are assigned to the new row col_sum.

#Finally, the new row and column values are swapped.

import numpy as np
import pandas as pd

def Sum_Swap( df ):
    minm_r = np.min(df, axis=1)  # Get minimum elements from all rows

    maxm_r = np.max(df, axis=1)  # Get maximum elements from all rows

    df['row_sum'] = minm_r + maxm_r  # Add the min & max values and assign them to new column

    minm_c = np.min(df, axis=0)  # Get minimum elements from all columns

    maxm_c = np.max(df, axis=0)  # Get maximum elements from all columns

    df.loc['col_sum'] = minm_c + maxm_c  # Add the min & max values and assign them to new row

    a, b = df['row_sum'].copy(), df.loc['col_sum'].copy()  # Store values of row and column in temparory variables

    df['row_sum'], df.loc['col_sum'] = b, a  # Interchange the values

    return df


# Test Code

df = pd.DataFrame(np.random.randint(1, 100, 25).reshape(5, 5))

df_res = Sum_Swap(df.copy())

print(df_res)