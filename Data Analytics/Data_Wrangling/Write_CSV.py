
'''The to_csv(file_name) function is used from the DataFrame object to save the data from the DataFrame object to the csv file.
 If the file does not exist, this function first creates the file and then writes data to it.'''

import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(25).reshape(5,5), columns = ['A','B','C','D','E'])

df.to_csv('/home/pooja/PycharmProjects/python_exercise/Data Analytics/Data_Wrangling/mytest.csv')