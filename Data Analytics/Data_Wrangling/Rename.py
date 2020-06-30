'''
There are several cases where we need to change the index names or values to indicate new or improved data.
 There are other methods, but the rename() function of pandas is used to perform this task efficiently.
'''


import numpy as np
import pandas as pd

df = pd.DataFrame(abs(np.random.randn(9)).reshape(3,3),
                          index = ['row1', 'row2', 'row3'],
                          columns = ['col1', 'col2', 'col3'])
print("The original DataFrame\n", df, '\n')
print("All row and column indexes are changed")
print(df.rename(index = str.upper, columns = str.title), '\n')

print("Specific row and column indexes are changed")
print(df.rename(index = {'row3':'row_index3'}, columns = {'col3':'col_index3'}))