
## NaN refers to null values in pandas. It usually occurs for those values that are not yet determined or defined.
# Suppose a new column needs to be added whose values are yet to be confirmed; all row values for the new column are null.

# The following example shows its working:

import pandas as pd

df = pd.read_csv('Cancer_data.csv')
# Assign new Disease column
new_df = pd.DataFrame(df, columns=['Sex', 'Under 1', '40-44', 'Disease'])

print("The new DataFrame with an added columns is:\n")
print(new_df.head())

# The NaN values can be assigned data in the following way:

import numpy as np
import pandas as pd

df = pd.read_csv('test.csv')

new_df = pd.DataFrame(df, columns=['Sex', 'Under 1', '40-44', 'Disease'])

new_df['Disease'] = "Lymphoma"
print("The new DataFrame is:\n")
print(new_df.head())

new_df2 = pd.DataFrame(df, columns=['Sex', 'Under 1', '40-44', 'Random_ID'])

new_df2['Random_ID'] = np.arange(new_df2.shape[0])

print("\nThe new DataFrame is:\n")
print(new_df2.head(10))

# The arange() method of NumPy is used on Line 14 to generate and assign numbers starting from 0 to the row count of DataFrame.
# The df.shape() method returns the dimensions of the DataFrame,
# and df.shape[0] returns the row count. The total row count is passed as a parameter to generate numbers until that row count value.