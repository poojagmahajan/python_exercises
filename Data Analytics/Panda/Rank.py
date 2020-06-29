
## Rank is basically the positioning of indexes according to the sorted values of a series.
# In simpler words, rank is assigned to the indexes from 1 to n, based on the value corresponding to the index.
# This tells us which place the value takes in the series if the list was sorted.
# The following illustration might make it more clear:

import pandas as pd
import numpy as np

srs = pd.Series(np.random.randn(5))

print("The series:")
print(srs)
# Ranks before sorting
print("\nRanks before sorting:")
print(srs.rank())

srs = srs.sort_values()
# Ranks after sorting
print("\nRanks after sorting:")
print(srs.rank())