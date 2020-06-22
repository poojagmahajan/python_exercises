
## Find Min and Max from a 2-D NumPy Array


def getMinMax( arr ):
    res = []

    for i in range(arr.shape[0]):  # Traverse over each row # shape is used to get row count

        res.append(arr[i].min())  # Store minimum element in list

        res.append(arr[i].max())  # Store maximum element in list

    return res


# Test Code
arr = np.random.randint(1, 100, size=(5, 5))

print("The Original Array:")
print(arr)

res_arr = getMinMax(arr)

print("\nThe Resultant list with min & max values:")
print(res_arr)