class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class DeQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def add_Front(self, value):
        newnode = Node(value)
        if self.front == None and self.rear == None:
            self.rear = self.front = newnode
            self.count += 1
            print(self.rear.data)
        else:
            newnode.next = self.front
            self.front = newnode
            self.count += 1
        
    def add_Rear(self,value):
        newnode = Node(value)
        if self.front == None and self.rear == None:
            self.rear = self.front = newnode
            print(self.front.data)
            self.count += 1
        elif self.front != None and self.rear == None:
            ptr = self.front
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = newnode
            self.rear = newnode
            self.count += 1
        else:
            self.rear.next = newnode
            self.rear = newnode
            self.count += 1
        
    def rem_Front(self):
        if self.front == None:
            print("Dequeue is empty" )
            self.count -= 1
        elif self.front.next == None:
                ans = self.front.data
                self.front = None
                return ans
        else:
            ans = self.front.data
            self.front = self.front.next
            self.count -= 1
            return ans
        
    def remv_Rear(self):
        ptr = self.front
        follow = self.front
        if self.rear == None and self.front == None:
            print("Dequeue is empty" )
        else:
            # length = DeQueue.count(self)
            while ptr.next != None:
                follow = ptr
                ptr = ptr.next
            ans = ptr.data
            self.rear = follow
            print(self.rear.data)
            self.count -= 1
        return ans
        

    def show(self):
        ptr = self.front
        while ptr is not self.rear:
            print(ptr.data, end=" ")
            ptr = ptr.next
        print(ptr.data)

    def count(self):
        return self.count

    def find_head(self):
        return self.front

    def find_tail(self):
        return self.rear



dq = DeQueue()
dq.add_Rear(15)
# dq.add_Rear(16)
# dq.add_Front(14)
# dq.add_Rear(17)
# dq.show()

# dq.rem_Front()
# print(dq.remv_Rear())
# print(dq.remv_Rear())
# dq.show()