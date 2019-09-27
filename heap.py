from math import log

class Heap(object):
    def __init__(self, H=None):
        if H:
            self.arr = H
            self.height =  int(log(len(self.arr), 2))
            self.heapify(self.height-1)
        else:
            self.arr = []
            
    def swap(self, i, j):
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def heapify(self, h_t):
        if h_t < 0:
            return None
        layer = h_t
        while h_t < self.height:
            start = 2**(h_t)-1
            end = start+2**(h_t)
            for i in range(start, end):
                if 2*i+1 < len(self.arr):
                    if self.arr[i] < self.arr[2*i+1]:
                        self.swap(i, 2*i+1)
                else:
                    break
                if 2*i+2 < len(self.arr):
                    if self.arr[i] < self.arr[2*i+2]:
                        self.swap(i, 2*i+2)
                else:
                    break
            h_t += 1
        self.heapify(layer-1)

    # Add element in heap
    def add(self, element):
        self.arr.append(element)
        child_idx = len(self.arr)-1
        # Check if there is any voilantion of heap after adding element
        while child_idx > 0:
            parent_idx = int((child_idx - 1.0)/2)
            if self.arr[child_idx] > self.arr[parent_idx]:
                self.swap(child_idx, parent_idx)
                child_idx = parent_idx
            else:
                break

    # return max element(root) from heap and update heap
    def max(self):
        max_elt = self.arr[0]
        self.arr[0] = self.arr[-1]
        self.arr.pop()
        parent_idx, ch_idx = 0, 0
        # Check if there is any voilantion, after replacing root by last elt.
        while True:
            # Check parent has left root
            if 2*parent_idx+1 < len(self.arr):
                if self.arr[parent_idx] < self.arr[2*parent_idx+1]:
                    self.swap(parent_idx, 2*parent_idx+1)
                    ch_idx = 2*parent_idx+1
            else:
                break
            if 2*parent_idx+2 < len(self.arr):
                if self.arr[parent_idx] < self.arr[2*parent_idx+2]:
                    if ch_idx:
                        self.swap(parent_idx, 2*parent_idx+1)
                        self.swap(parent_idx, 2*parent_idx+2)
                        ch_idx = 2*parent_idx+2
                    else:
                        self.swap(parent_idx, 2*parent_idx+2)
                        ch_idx = 2*parent_idx+2
            else:
                break
            if ch_idx:
                parent_idx, ch_idx = ch_idx, 0
            else:
                break
        return max_elt

    # Print heap structre
    def structre(self):
        return self.arr


# adding elements in heap
# heap.add(5)
# heap.add(6)
# heap.add(7)
# heap.add(4)
# heap.add(13)
# heap.max()

# print heap.structre()

# Sort a random list using heap
import random

# Instance of Heap class

unsorted_arr = list(range(1,21))
random.shuffle(unsorted_arr)

print ('unsorted array:')
print (unsorted_arr) 
print ('') 

heap = Heap(unsorted_arr)
heap.add(0)

print ('heapify array:')
print (heap.structre()) 
print ('') 

sorted_arr = [heap.max() for _ in range(len(heap.structre())) ]

print ('sorted array:')
print (sorted_arr)
