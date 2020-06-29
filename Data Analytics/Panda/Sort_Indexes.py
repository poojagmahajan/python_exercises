
## Sort, as the name suggests, simply sorts a Series object in ascending order.

# sort_index(): This function sorts the indexes in ascending order.
# It works on the alphabetic, numeric, and alphanumeric indexes.
# The non-numeric index values are treated as corresponding ASCII codes and sorted accordingly.

import pandas as pd

# Numeric indexes
print("Numeric Indexes Sorted")
srs1 = pd.Series([1,2,3], index = ['3', '1', '2'])
print(srs1.sort_index())

# Alphabetic indexes
print("\nAlphabetic Indexes Sorted")
srs2 = pd.Series([1,2,3], index = ['B', 'C', 'A'])
print(srs2.sort_index())

# Alhanumeric indexes
print("\nAlphanumeric Indexes Sorted")
srs3 = pd.Series([1,2,3], index = ['3', '2', 'A'])
print(srs3.sort_index())
