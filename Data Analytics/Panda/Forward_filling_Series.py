

### Series ####

import pandas as pd

srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan'])
srs1.name = "Growth Rate"
srs1.index.name = "Country"

srs2 = srs1.reindex(['China', 'India', 'Malaysia', 'USA', 'Brazil', 'Pakistan', 'England'])
print("The series NaN Values:\n",srs2)

print("\nThe series with new Values:\n",srs2.ffill())
