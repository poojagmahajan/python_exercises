
# Link - https://seaborn.pydata.org/generated/seaborn.lmplot.html

'''
Regression is usually used to find the relationship between the dependent and independent variables of a dataset.
 Similarly, a regression plot helps us visualize the relationship of data in real time.
By successfully obtaining a regression line, analysts can use it to predict future trends of the data.

In the seaborn package, the lmplot function is used to generate regression plots. Seaborn also provides built-in datasets to test its functionalities.

We will use the tips dataset as used in its documentation( https://seaborn.pydata.org/generated/seaborn.lmplot.html )
 The data information about customers at a restaurant.
'''

import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('tips') # Loading dataset from seaborn library

sns1 = sns.lmplot(x = 'total_bill', y = 'tip',hue = 'sex', data = df) # plotting regression plot