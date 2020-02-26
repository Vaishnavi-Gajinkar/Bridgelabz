class node:
    def __init__(self, data=None):
        self.data = data
        self.nxt = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        if self.head == None:
            self.head = new_node
        else:
            while curr.nxt != None:
                curr = curr.nxt
            curr.nxt = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.nxt != None:
            total += 1
            curr = curr.nxt
        return total

    def display(self):
        elems=[]
        curr = self.head
        while curr.nxt != None:
            curr = curr.nxt
            elems.append(curr.data)
            print(elems)

    def get(self, indx):
        if indx >= self.length():
            print("Error! Index out of range")
            return None
        curr = self.head
        count = 0
        while indx != count:
            curr = curr.nxt
            count += 1
        return curr.data


#myList = LinkedList()


#myList.display()

#myList.append(1)
#myList.append(2)
#myList.append(3)
#myList.append(4)

#myList.display()

#x = myList.get(5)
#print("Element at pos is ", x)
#myList.display()
#print(myList.length())
