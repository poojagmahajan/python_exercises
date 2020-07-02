'''
 The agg() function provides a lot of other functionalities, some of which are listed in the table below.
max -	Computes the max of the grouped values
min	- Computes the min of the grouped values
last -	Computes the last of the grouped values
first -	Computes the first of the grouped values
sum	 - Computes the sum of the grouped values
size -	Computes the size or length of the grouped values
count -	Computes the count of the grouped values
var	 - Computes the variance of the grouped values
std -	Computes the standard deviation of the grouped values
describe -	Provides the descriptive statistics about the grouped values
'''
# Eg. Some random animals are defined with hypothetical legs, weight, height, and protein values.
#  Our task is to compute the average amount of legs, weight, height, and protein a certain animal class can have.
import numpy as np
import pandas as pd
import random
# Declaring a DataFrame with values
df = pd.DataFrame({'Animal_type':[random.choice(['Chicken','Duck', 'Goat', 'Turkey']) for i in range(1,16)],
                   'legs':[random.choice(range(1,4)) for i in range(1,16)],
                   'weight':[random.choice(range(10,20)) for i in range(1,16)],
                   'height':[random.choice(range(4,15)) for i in range(1,16)],
                   'protein':abs(np.random.randn(15)),
                    })
print("The Original DataFrame:")
print(df, '\n*******************************************')

Animal = df.groupby('Animal_type') # Grouping with Animal_type column

# Computing mean of individual groups
print("Average properties an animal can have:")
print(Animal.agg('mean'), '\n*******************************************')  ## agg is an alias for aggregate.

df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [np.nan, np.nan, np.nan]],
                  columns=['A', 'B', 'C'])
print(df)
# Aggregate these functions over the rows.
print(df.agg(['sum', 'min']),'\n******************')
# Different aggregations per column.
print(df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']}),'\n******************')
# Aggregate over the columns.
print(df.agg("mean", axis="columns"),'\n******************')