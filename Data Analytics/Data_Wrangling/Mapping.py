
''' this technique is used to map the values of a Series or a DataFrame.
The current values in a Series or a DataFrame are made equivalent to some other values.
 Then, the pandas map function is used to either replace the mapped values or join them together.
  The map() function can also be used to fill in the values of new columns.'''

import pandas as pd

df = pd.DataFrame({'City':['Lahore', 'Mumbai', 'Karachi', 'London'],
                   'AQI':[147, 166, 152, 81]})

print("The Original DataFrame")
print(df,'\n')

dict_map = {'Lahore':'Pakistan', 'Karachi':'Pakistan', 'Mumbai':'India', 'London':'UK'}

df['Country'] = df['City'].map(dict_map)

print("The Mapped DataFrame")
print(df)