
'''
Defination - NumPy can be defined as an interactive Python package for array processing,
             and it is mostly used to perform scientific programming.
List vs numpy array - less memory
                     faster
                     convinient
                     Cannot append new values like lists
                     Size and type of array is fixed
'''

import numpy as np
n1_array = np.array([1,2,3,4,5])  # 1 - D array

n2_array = np.array([ [1,2,3,4,5],[5,4,3,2,1] ])   # 2 - D array

print(n1_array)
print(n2_array)

##    IMP functions ##

print("An Empty Array of size 5")
print(np.empty(5)) # Generate empty array of size 5

print("An Array of only 1's of size 5")
print(np.ones(5)) # Generate array containing only 1's of size 5

print("An Array of only 0's of size 5")
print(np.zeros(5)) # Generate array containing only 0's of size 5

print("An Identity Matrix Array of size 5")
print(np.eye(5)) # Generate identity matrix array of size 5

print("Array populated with numbers from 2 to 50 with the difference of 3")
print(np.arange(2, 50, 3)) # Generate array with consecutive numbers  (start,end,diif)