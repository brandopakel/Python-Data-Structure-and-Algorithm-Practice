class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        node = self.head
        while(node):
            print(node.data)
            node = node.next


llist = LinkedList()
for i in range(0,100):
    llist.append(Node(i))
print (node.value for node in llist)