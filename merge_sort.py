# It is the implementation of recursive merge sort

import random
arr = range(10)
random.shuffle(arr)
print 'Unsorted arr:', arr

# Merging Function
def merge(l_arr, r_arr):
	res = []
	l,r = 0,0
	while l<len(l_arr) and r<len(r_arr):
		if l_arr[l]>r_arr[r]:
			res.append(r_arr[r])
			r += 1
		else:
			res.append(l_arr[l])
			l += 1
	res += r_arr[r:] if l==len(l_arr) else l_arr[l:]
	return res

def merge_sort(arr):
	if len(arr) == 1:
		return arr
	mid = len(arr)/2
	l_arr = merge_sort(arr[:mid])
	r_arr = merge_sort(arr[mid:])
	return merge(l_arr, r_arr)

print 'sorted arr:',merge_sort(arr)
