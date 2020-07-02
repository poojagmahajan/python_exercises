
'''Anything that lies outside the normal distribution of the provided dataset is known as an outlier.'''

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(900,3))

quantiles_df = (df.quantile([0.25,0.75]))

print("The 1st & 3rd quartiles of all columns:")
print(quantiles_df, '\n*******************************************')

Q1 = quantiles_df[0][0.25]
Q3 = quantiles_df[0][0.75]

iqr = Q3 - Q1

lower_bound = (Q1 - (iqr * 1.5))
upper_bound = (Q3 + (iqr * 1.5))

print("The Lower bound for the first column:")
print(lower_bound, '\n*******************************************')

print("The Upper bound for the first column:")
print(upper_bound, '\n*******************************************')

col1 = df[0]

print("The outliers in the first column below the lower bound:")
print(col1[(col1 < lower_bound)], '\n*******************************************')

print("The outliers in the first column above the upper bound:")
print(col1[(col1 > upper_bound)], '\n*******************************************')