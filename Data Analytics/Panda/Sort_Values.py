
##sort_values() This function sorts the values of a Series.
# This can sort both the alphabetic and numeric values.
# Just like the sort_index() method, the non-numeric values are treated as ASCII characters.

import pandas as pd
import numpy as np

# Numeric values
print("Random Numeric Values Sorted")
srs1 = pd.Series(np.random.randn(5))
print(srs1.sort_values())

# Alphabetic values
print("\nAlphabetic Values Sorted")
srs2 = pd.Series(['D', 'A', 'E', 'C', 'B'])
print(srs2.sort_values())