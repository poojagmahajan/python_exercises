
'''
This visualization is used to display groups of statistical or numerical data using their quantiles.
These plots have lines extended from them known as whiskers.
'''
import numpy as np

import seaborn as sns

set1 = np.random.randn(220) # Generating random data

sns1 = sns.boxplot(set1) # plotting box plot

sns1 = sns.boxplot(set1, whis=np.inf)  # The whis parameter is used and assigned a value of np.inf, meaning infinity