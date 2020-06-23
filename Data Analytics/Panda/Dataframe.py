
import pandas as pd

df = pd.read_csv('Cancer_data.csv') # Read from csv file

print (df.head()) ## # This method prints the first five rows in the dataframe

print(df.tail(6))  # it prints 6 end lines

# The pandas DataFrame object provides methods to select specific columns from it.
# The following example shows how it can be done.


df = pd.read_csv('Cancer_data.csv')

print(df.columns) # print columns of DataFrame

print("\nThe First Column")
print(df['Sex'].head()) # Fetch the sex colum from DataFrame
print("\nThe type of this column is: " + str(type(df['Sex'])) + "\n")

print("\nThe Second Column")
print(df['Under 1'].head()) # Fetch the Under 1 colum from DataFrame
print("\nThe type of this column is: " + str(type(df['Under 1'])) + "\n")


print("\nThe Last Column")
print(df['40-44'].head()) # Fetch the 40-44 colum from DataFrame
print("\nThe type of this column is: " + str(type(df['40-44'])) + "\n")

## Multiple columns can also be grabbed to make an entirely new DataFrame object.
# The following example shows how it can be done.

df = pd.read_csv('test.csv')
print(df.columns)

print("\nThe original DataFrame:")
print(df.head())

print("\nThe new DataFrame with selected columns is:\n")
new_df = pd.DataFrame(df,columns =['Sex', 'Under 1', '40-44'])

print(new_df.head())

## pandas also provide functionalities to access the row information from the Dataframe.
# The function loc[n] can be used to fetch row data at index n.
# The loc[n] method returns a Series with column names as indexes and row data as their values.

df= pd.read_csv('Cancer_data.csv')

print("\nThe Row values at index 0\n")
print(df.loc[0])

print("\nThe Row values at index 1\n")
print(df.loc[1])

print("\nThe Row values at index 6\n")
print(df.loc[6])