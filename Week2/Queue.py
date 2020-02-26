class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.rear = None
    
    def enq(self,value):
        newnode = node(value)
        if self.rear == None:
            self.head = self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode

    def deq(self):
        if self.head == None:               #Queue is empty
            print("Queue is empty")
        else:
            if self.head.next == None:      #Queue has only one element
                ans = self.head.data
                self.head = self.head.next
            else:
                ans = self.head.data
                self.head = self.head.next  #removing one element from head
        return ans
    
    def is_Empty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        ptr = self.head
        count = 0
        while ptr != self.rear:
            count +=1
        return count+1

    def show(self):
        ptr = self.head
        if ptr == None:
            print("Queue empty. Nothing to show")
        print("Displaying elements of queue")
        while ptr.next != None:
            print(ptr.data, end=",")
            ptr = ptr.next
        print(ptr.data, end='\n')

