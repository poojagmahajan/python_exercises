
##  This method allows for adding new indexes and columns in Series and DataFrames without disturbing the initial setting of the objects.

# The function used for this purpose is reindex(). It is called by a Series or a DataFrame object, and a list of indexes is passed as a parameter.

#  Re-indexing rules are the same for both Series and DataFrame objects.

####  Series   ####

#importing pandas in our program
import pandas as pd

# Defining a series object
srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan'])

# Set Series name
srs1.name = "Growth Rate"

# Set index name
srs1.index.name = "Country"

srs2 = srs1.reindex(['China', 'India', 'Malaysia', 'USA', 'Brazil', 'Pakistan', 'England'])
print("The series with new indexes is:\n",srs2)

srs3 = srs1.reindex(['China', 'India', 'Malaysia', 'USA', 'Brazil', 'Pakistan', 'England'], fill_value=0)
print("\nThe series with new indexes is:\n",srs3)

###### Dataframe  ######

import numpy as np
import pandas as pd

# Define a 2-D array
arr2d = np.arange(16).reshape(4,4)

# Give 2-D array to Dataframe and assign index and column names.
df = pd.DataFrame(arr2d, index=['Row1', 'Row2', 'Row4', 'Row5'], columns=['Column1','Column2','Column3','Column4'])
print("The original DataFrame\n", df)

df2 = df.reindex(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])
print("\nNew DataFrame with reindexed indexes:\n", df2)

df2 = df2.reindex(columns=['Column0', 'Column1', 'Column2', 'Column3', 'Column4'])
print("\nNew DataFrame with reindexed columns:\n", df2)