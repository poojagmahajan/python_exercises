
''' Series can be described as a single column of a 2-D array or a matrix.
 It has specific index values attached to each row for identification.
 It can also be imagined as one column of an excel file.'''

# importing pandas in our program
import pandas as pd

# Defining a series object
srs = pd.Series([1,2,3,4,5])

# printing series values
print("The Series values are:")
print(srs.values)

# printing series indexes
print("\nThe Index values are:")
print(srs.index.values)

# Let’s look at an example where the population growth rate of different countries is assigned to the country name.


# Defining a series object
srs = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan'])

# Set Series name
srs.name = "Growth Rate"

# Set index name
srs.index.name = "Country"

# printing series values
print("The Indexed Series values are:")
print(srs)

#importing pandas in our program
import pandas as pd
# Defining two series object
srs1 = pd.Series([11.9, 36.0, 16.6, 21.8, 34.2, 62.4], index = ['China', 'India', 'USA', 'Brazil', 'Pakistan', 'Nigeria'])
srs2 = pd.Series([20.3, 11.9, 36.0, 16.6, 21.8, 34.2], index = ['Africa', 'China', 'India', 'USA', 'Brazil', 'Pakistan'])
# Dividing series 1 values with seies 2 values
srs = srs1 / srs2
# Set Series name
srs.name = "Resultant Object"
# Set index name
srs.index.name = "Country"

############

print("The indexes that are assigned ‘True’ are Null:")
print(pd.isnull(srs))

print("\nThe indexes that are assigned ‘True’ are not Null:")
print(pd.notnull(srs))

print("\nIndexes that satisfy the condition are:")
print(srs[srs == 1.0])

print("\nIndexes that satisfy the condition are:")
print(srs[srs != 1.0])