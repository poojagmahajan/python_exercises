
import numpy as np

arr1 = np.random.rand(7)  # random(generate array with random numbers
arr2 = np.array(['Dog', 'Cat', 'Lion', 'Dog', 'Eagle', 'Turtle', 'Lion'])

print("The original array")
print(arr1)

print("\nMean of all elements of array")
print(arr1.mean())

print("\nVariance of all elements of array")
print(arr1.var())

print("\nStandard Deviation of all elements of array")
print(arr1.std())

print("\nSum of all elements of array")
print(arr1.sum())

print("\nSorted array")
arr1.sort()
print(arr1)

print("\nOriginal array")
print(arr2)

print("\nUnique array")
print(np.unique(arr2))

# where function

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([500, 600, 700, 800])

cond = np.array([False, True, False, True]) # Create an array with bool operators

res = np.where(cond, arr1, arr2) # apply the where condition
print(res)