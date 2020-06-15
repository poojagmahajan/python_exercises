

'''Binary search assumes that the array on which the search will take place is sorted in ascending order.
In binary search, the target element is compared with the middle element of the array
following which the next chunk of the array to be searched is decided. If the target matches the middle element,
we are successful. Otherwise, since the array is sorted, if the target is smaller than the middle element,
 it could only be in the left half of the array. Alternatively, if the target is greater than the middle element,
 it could be in the right half of the array.
 So, we exclude one half of the array from the further search and repeat the same strategy to the remaining half.'''

def linear_search(data,target) :
    for i in range (len(data) ):
        if data[i] == target :
            return True
        else:
            return False

def binary_search_iterative(data,target) :
    low = 0
    high = len(data) -1

    while low < high : ## should be sort in ascending order
        mid = (low + high ) // 2
        if data[mid] == target :
            return true
        elif target < data[mid] :
            high = mid - 1
        else :
            low = mid +1
    return  False

def binary_search_recursive(data, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return binary_search_recursive(data, target, low, mid-1)
		else:
			return binary_search_recursive(data, target, mid+1, high)
data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
target = 37

print(binary_search_recursive(data, target, 0, len(data)-1))
print(binary_search_iterative(data, target))

