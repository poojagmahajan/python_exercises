
'''CSV stands for comma separated values. These are the most common and widely used files with pandas DataFrame object.
It is a kind of a text file that uses the extension .csv instead of .txt.
Text is separated by commas , in this file, and when a DatFrame reads this file,
values between commas become cell values of the DataFrame.

The pandas package provides both reading and writing functions for csv files.
'''

import pandas as pd

df = pd.read_csv('test.csv') # reading csv file # you can give file's path instead of file
print(df)

df = pd.read_csv('test.csv', header = None) # reading csv file without headers
print('\n',df)

#If header = None parameter is not passed to the read_csv function,
# the first row in the file is considered to be the column names.
# If it is passed as a parameter then,it treats the first row as data and automatically generates the column names as done for indexes.
# Look in o/p