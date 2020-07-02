
'''
The task is to reshape the DataFrame using the pivot function and plot it on a heatmap just like explained here.
The year column of the dataset will be set as columns, the month will be set as row indexes, and the passengers will be the values.
 After reshaping, use the heatmap function of seaborn to plot the visualization.
'''

#### Heatmap ###############

import pandas as pd
import seaborn as sns

df = sns.load_dataset('flights') # Reading flights dataset from seaborn package
# Reshaping the DataFrame
df = pd.pivot_table(df, values = 'passengers', index = ['month'], columns = 'year')

# Plotting the heatmap
sns.heatmap(df, annot = True, fmt = '')   ## The fmt parameter keeps the numbers on the heatmap concise for a better view and understanding.

