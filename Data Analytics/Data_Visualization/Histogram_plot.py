
# Referal Links - https://seaborn.pydata.org/generated/seaborn.jointplot.html
#                 https://matplotlib.org/api/_as_gen/matplotlib.pyplot.hist.html
#                 https://seaborn.pydata.org/examples/index.html
#                 https://seaborn.pydata.org/tutorial.html
'''
This visualization is used to display the distribution of numerical data as accurately as possible.
 This plot divides the data into a specified number of bins, thus separating the data into a range of values.
 Then, it sketches bars to show the number of data points that each bin contains.
'''
###############  Using matplotlib  #####################

# Matplotlib provides the hist() function to plot a histogram.

import numpy as np
import matplotlib.pyplot as plt

set1 = np.random.randn(200) # generating normal data

plt.hist(set1,bins =20,color='red',density= True )

# Multiple histograms

set1 = np.random.randn(200)
set2 = np.random.randn(150)
# ploting histograms
plt.hist(set1, density=True, color='red', alpha=0.6,bins=20)
plt.hist(set2, density=True, alpha=0.6,bins=20)  # alpha parameter introduced here makes the respective plots transparent to a specific percentage assigned to it.

########### Using seaborn ######################

# jointplot() function is used for this task.

import numpy as np
import seaborn as sns

set1 = np.random.randn(500)
set2 = np.random.randn(500)

sns1 = sns.jointplot(set1, set2)

sns2 = sns.jointplot(set1, set2, kind='hex')  # Data in hexagonal form
# kind parameters are scatter, reg, resid, or kde