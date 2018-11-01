# Stack and Queue implementations 

class Stack(object):
	def __init__(self, arg=[]):
		self.arg = arg
		
	def push(self, element):
		self.arg.append(element)

	def pop(self):
		return self.arg.pop()



class Queue(object):
	def __init__(self, arg=[]):
		self.arg = arg
		
	def enqueue(self, element):
		self.arg.append(element)

	def dequeue(self):
		temp = self.arg[0]
		self.arg = self.arg[1:]
		return temp
		

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.pop()
s.push(4)
print (s.arg)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(4)
print (q.arg)