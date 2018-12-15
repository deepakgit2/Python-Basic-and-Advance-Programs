class Node(object):

	def __init__(self, value):
		self.value = value
		self.next = None


class LinkedList(object):

	def __init__(self, head = None):	
		self.head = head

	def add(self, new_element):
		node = Node(new_element)
		if self.head == None:
			self.head = node
		else:
			node.next = self.head
			self.head = node

	def insert(self, new_element, position):
		obj2 = self.head
		n_obj = Node(new_element)

		if position == 1:
			n_obj.next = obj2
			self.head = n_obj
			return
		
		for i in range(1, position-1):
			obj2 = obj2.next

		n_obj.next = obj2.next
		obj2.next = n_obj


	def delete(self, element):
		obj = self.head
		if obj == None:
			return 'Linked list is empty'

		elif obj.value == element:
			self.head = obj.next
			return None
	
		while obj.next != None:
			if obj.next.value == element:
				obj.next = obj.next.next
				return None
			obj = obj.next
		else:
			if obj.value == element:
				obj = None
				return None
		raise IndexError('Element should be present in linked list')



				


linked_list = LinkedList()
ll = []


for i in range(1,6):
	linked_list.add(i)
print ('added number (1 to 5) in lnked list\n')
linked_list.insert(15, 3)
obj = linked_list.head

print ('inserted 15 at 3rd position in lnked list\n')
terminator = 0
while obj.next != None:
	# print obj.value
	ll.append(obj.value)
	obj = obj.next
	terminator += 1
	if terminator > 8:
		print 'terminator working'
		break
else:
	# print obj.value
	ll.append(obj.value)

print ('visulaization of linked list\n')
print ll



		
