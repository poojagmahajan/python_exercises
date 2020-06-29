
# select elements based on the index name or index number.

import numpy as np
import pandas as pd

srs = pd.Series(np.arange(0, 6, 1), index = ['ind0', 'ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
srs.index.name = "Index"
print("The original Series:\n", srs)

print("\nSeries element at index ind3:")
print(srs['ind3']) # Fetch element at index named ind3

print("\nSeries element at index 3:")
print(srs[3]) # Fetch element at index 3

print("\nSeries elements at multiple indexes:\n")
print(srs[['ind1', 'ind4']]) # Fetch elements at multiple indexes

# Select Range of elements

print("\nSeries elements after and including index 4:\n", srs[4: ]) # Fetch elements in a range

print("\nAll Series elements greater than equal to 3:\n", srs[srs >= 3]) # Fetch elements with a condition

### Dropping an unwanted index from the Series object is also an important function.
# If the drop(index_name) function is called with a given index on a Series object,
# the desired index name is deleted from the Series.

import numpy as np
import pandas as pd

srs = pd.Series(np.arange(0, 6, 1), index = ['ind0', 'ind1', 'ind2', 'ind3', 'ind4', 'ind5'])
srs.index.name = "Index"
print("The original Series:\n", srs)

srs = srs.drop('ind2') # drop index named ind2

print("The New Series:\n", srs)