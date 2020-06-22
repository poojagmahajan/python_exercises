
##  Indexing 1 D array
import numpy as np

arr = np.arange(0,10,1) # Generate array with numbers from 0 to 9
print("The Array")
print(arr)

print("\nElement at index 5")
print(arr[5]) # Fetch element at index 5

print("\nElements in a range of 0 to 6")
print(arr[0:6]) # Fetch elements in a range

arr[0:6] = 20 # Assign a value to a range of elements
print("\nNew array after changing elements in a range of 0 to 6")
print(arr)

## Slicing of 1 - D array

arr = np.arange(0,10,1)
print("The Array")
print(arr)

new_arr1 = arr[1:7] # This command selects a range of elements from the array
print("\nThe new sliced array")
print(new_arr1)

new_arr2 = arr[:] # This command selects all elements in the array
print("\nThe new sliced array with all elements")
print(new_arr2)

##  Indexing 2 D array


arr2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])                           # Declare a 2-D array
print("The Array")
print(arr2d)

print("\nElement at row 0 and column 1")
print(arr2d[0][1])

print("\nElements in a range of last two rows & columns")
print(arr2d[1:3, 1:3])

arr2d[1:3, 1:3] = 20
print("\nNew 2D array after changing last two rows & columns values")
print(arr2d)

## Slicing of 2 - D array

arr2d = np.array([
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
])
print("The Array")
print(arr2d)

print("\nThe new sliced array")
print(arr2d[1:3, 0:2])

print("\nThe new sliced column")
print(arr2d[:, 1:2])
