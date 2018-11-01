# Python implementation of max_Heap data structre


class Heap(object):
	def __init__(self, arr = []):
		self.arr = arr

	# Add element in heap
	def add(self, element):
		self.arr.append(element)
		child_idx = len(self.arr)-1

		# Check if there is any voilantion of heap after adding element
		while child_idx > 0:
			parent_idx = int((child_idx - 1.0)/2)
			if self.arr[child_idx] > self.arr[parent_idx]:
				temp = self.arr[child_idx]
				self.arr[child_idx] = self.arr[parent_idx]
				self.arr[parent_idx] = temp

				child_idx = parent_idx
			else:
				break

	# return max element(root) from heap and update heap
	def max(self):
		max_elt = self.arr[0]
		self.arr[0] = self.arr[-1]
		self.arr.pop()

		parent_idx = 0
		# Check if there is any voilantion, after replacing root by last elt.
		while True:
			# Check parent has left root
			try:
				left_child = self.arr[2*parent_idx+1]
			except IndexError:
				break

			# Check parent has right root
			try:
				right_child = self.arr[2*parent_idx+2]
			except IndexError:
				ch_idx = 2*parent_idx+1

			else:
				# Find index of bigger child 
				if left_child < right_child:
					ch_idx = 2*parent_idx+2
				else:
					ch_idx = 2*parent_idx+1
			
			# If child is bigger than parant then swap
			if self.arr[parent_idx] < self.arr[ch_idx]:
				temp = self.arr[parent_idx]
				self.arr[parent_idx] = self.arr[ch_idx]
				self.arr[ch_idx] = temp
			else:
				break
			parent_idx = ch_idx

		return max_elt

	# Print heap structre
	def structre(self):
		return self.arr

# Instance of Heap class
heap = Heap()


# # adding elements in heap
# heap.add(5)
# heap.add(6)
# heap.add(7)
# heap.add(4)
# heap.add(13)
# heap.max()

# print heap.structre()



# Sort a random list using heap
import random

heap = Heap()
unsorted_arr = list(range(1,21))
random.shuffle(unsorted_arr)

print ('unsorted array:')
print (unsorted_arr) 
print ('') 

for elt in unsorted_arr:
	heap.add(elt)

print ('heapify array:')
print (heap.structre()) 
print ('') 

sorted_arr = [heap.max() for _ in range(len(heap.structre())) ]

print ('sorted array:')
print (sorted_arr)