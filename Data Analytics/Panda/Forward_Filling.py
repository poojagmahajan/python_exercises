

###   This is a way of assigning values to the default NaN that occurs due to re-indexing.

### Series ####

import pandas as pd

srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan'])
srs1.name = "Growth Rate"
srs1.index.name = "Country"

srs2 = srs1.reindex(['China', 'India', 'Malaysia', 'USA', 'Brazil', 'Pakistan', 'England'])
print("The series NaN Values:\n",srs2)

print("\nThe series with new Values:\n",srs2.ffill())

## Dataframe ####

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape(4,4), index=['Row1', 'Row2', 'Row4', 'Row5'], columns=['Column1','Column2','Column3','Column4'])

df2 = df.reindex(['Row1', 'Row2', 'Row3', 'Row4', 'Row5'])
df2 = df2.reindex(columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5'])
print("DataFrame with NaN Values:\n", df2)

# Fill values row wise
print("\nDataFrame with new values around Axis 0:\n", df2.ffill(axis = 0))

# Fill values column wise
print("\nDataFrame with new values around Axis 1:\n", df2.ffill(axis = 1))

##  For rows, the values above the NaN are copied, and for columns, the values to the left are copied.