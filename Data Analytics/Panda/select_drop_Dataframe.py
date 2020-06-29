

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(16).reshape(4,4), index=['Row1', 'Row2', 'Row3', 'Row4'], columns=['Column1','Column2','Column3','Column4'])

print("The original DataFrame\n", df)

print("\nElements which satisfy the condition:\n", df[df['Column3'] > 6])

print("\nElements of Index named Row4:\n", df.loc['Row4'])  ##The function loc[n] can be used to fetch row data at index n

### Drop

#df = pd.DataFrame(np.arange(16).reshape(4,4), index=['Row1', 'Row2', 'Row3', 'Row4'], columns=['Column1','Column2','Column3','Column4'])

print("The original DataFrame\n", df)

print("\nDataFrame after dropping Index Row2:\n", df.drop('Row2'))

print("\nDataFrame after dropping Column2:\n", df.drop('Column2',axis=1))