'''

Grouping arranges similar data of a DataFrame in groups.
The groupby function is used for this task.
The values of the DataFrame can be grouped on both single and multiple columns.
'''

import numpy as np
import pandas as pd

df = pd.DataFrame({'p1':['A','A','B','B','C','C'],'p2':['G1','G2','G1','G2','G1','G2'],
    'val_1':np.random.randn(6),'val_2':np.random.randn(6)})

print("original dataframe :")
print(df)

print("DataFrame after using groupby :")
print(df.groupby('p1'))

# Grouping on Multiple columns

df = pd.DataFrame({'p1':['A','A','B','B','C','C'],'p2':['G1','G2','G1','G2','G1','G2'],
    'val_1':np.arange(1,7,1),'val_2':np.arange(7,13,1)})

print("The original DataFrame")
print(df, '\n*******************************************')

# For a valid-grouped DataFrame to be returned, an operation such as summation or averaging needs to be performed on the grouped data.
print("DataFrame after using groupby on p1 and summing the values")
print(df.groupby('p1').sum(), '\n*******************************************')

print("DataFrame after using groupby on p2 and summing the values")
print(df.groupby('p2').sum(), '\n*******************************************')

print("DataFrame after using groupby on p1 & p2 ",'\n****************************')
print(df.groupby(['p1','p2']))

print("DataFrame after using groupby on p1 & p2 and Summing their values")
print(df.groupby(['p1','p2']).sum(), '\n*******************************************')