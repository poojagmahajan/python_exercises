
import numpy as np
# Creating 2-D array
arr = np.arange(0,50,1).reshape(10,5) # Declare a 2-D array

print("The original array")
print(arr)

print("\nThe transposed array")
print(arr.transpose()) # Print the transposed array
#print(arr.T) # This can also be used and same result will be produced

# Declare 2 array
arr1 = np.arange(1,40,4)
arr2 = np.arange(1,30,3)

print("The first array\n", arr1, "\nThe second array\n", arr2, '\n')

print("The Exponent Function")
print(np.exp(arr1))

print("\nThe Square Function")
print(np.square(arr1))

print("\nThe Square root Function")
print(np.sqrt(arr1))

print("\nThe Cube root Function")
print(np.cbrt(arr1))

print("\nThe Addition Function")
print(np.add(arr1, arr2))

print("\nThe Subtraction Function")
print(np.subtract(arr1, arr2))