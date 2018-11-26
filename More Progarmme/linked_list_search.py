class node:
    def __init__(self,data,link=None):
        self.data = data
        self.n_node = link
    
    def n_data(self):
        return self.n_node
    
    def data_part(self): #returns data part in node
        return self.data

class link: # provide linked list
    def __init__(self, head=None):
        self.head = head
        self.c_size = 0

    def add(self,d):
        temp = node(d,self.head)
        self.head  =temp
        self.c_size = self.c_size+1

    def size(self): #size of linked list
        return self.c_size

    def search (self, d): #find element
        c_node = self.head
        while c_node:
            if c_node.data_part() == d:
                return 'Exist'
            else:
                c_node = c_node.n_data()
        return 'Not Exist'
    def linked_list_output(self): #linked list as list
        a = []
        c_node = self.head
        for i in range(self.c_size):
            a += [c_node.data_part()]
            print c_node.data_part()
            c_node = c_node.n_data()
        return a
            
linked_list = link()
linked_list.add('ram')
linked_list.add('shyam')
linked_list.add('seeta')
linked_list.add('rahul')
print linked_list.size()
print linked_list.search('seeta')
