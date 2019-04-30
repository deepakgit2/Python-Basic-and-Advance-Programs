# It is the implementation of recursive merge sort

import random
arr = range(10)
random.shuffle(arr)
print ('Unsorted arr:', arr)

# Merging Function
def merge(arr1, arr2):
	temp_arr = []
	while len(arr1) and len(arr2):
		if arr1[0] <= arr2[0]:
			temp_arr.append(arr1[0])
			arr1 = arr1[1:]
		else:
			temp_arr.append(arr2[0])
			arr2 = arr2[1:]
	return temp_arr + arr1 + arr2

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	mid = len(arr)/2
	l_arr = merge_sort(arr[:mid])
	r_arr = merge_sort(arr[mid:])
	return merge(l_arr, r_arr)

print ('Sorted arr:',merge_sort(arr))
