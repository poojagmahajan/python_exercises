

'''A scatter plot represents the values of data as points in a cartesian plane.
It displays the data points based on the cartesian coordinates on an XY-plane.
It is preferably used when a pair of dependent and independent variables need to be represented or visualized
Same like regression plot
'''

import numpy as np
import seaborn as sns

df = sns.load_dataset('tips')

sns1 = sns.scatterplot(x = 'total_bill', y = 'tip', data = df)

##### KDE (kernel density estimation) plots #######

# This function calculates and plots the probability density of a given dataset,
# which means that it estimates the value of a random variable.

import numpy as np
import seaborn as sns

x = np.random.randn(100) # Generating random data

sns1 = sns.kdeplot(x, color = 'red') # ploting KDE plot