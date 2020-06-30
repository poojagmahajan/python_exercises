
import pandas as pd

df = pd.DataFrame({'Col1':['A', 'B', 'A', 'C', 'B', 'C'],
                    'Col2': [1, 2, 1, 3, 4, 3]})

print("The Original DataFrame")
print(df,'\n')

print("The DataFrame without duplicates")
print(df.drop_duplicates(),'\n')

print("The DataFrame without Column1 duplicates")
print(df.drop_duplicates(['Col1']))