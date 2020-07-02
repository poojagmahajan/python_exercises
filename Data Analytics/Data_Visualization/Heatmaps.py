'''
Wherever data needs to be displayed efficiently, and in a comprehensible manner, heatmaps are used.
They visualize trends in data perfectly and enable us to analyze what to do next.
A heatmap uses different colors to display data, while other plotting methods either use height or width parameters for it.
 Specific colors in varying concentrations are applied to different values of data depending on their importance.
'''

import pandas as pd
import seaborn as sns

# predefined table in data variable
df = pd.read_csv('Data.csv')
# Reshaping DataFrame
df = pd.pivot_table(df, values='lifeExp', index=['continent'], columns='year')

sns1 = sns.heatmap(df) # plotting heatmap

## Annotation

# This method of seaborn allows the user to view the data points as well as the color band to which they belong.

sns1 = sns.heatmap(df, annot = True) # Using annotation to display numbers