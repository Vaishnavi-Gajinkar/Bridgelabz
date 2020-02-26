#f = open("Numbers.txt",'r+')
#for line in f:

class node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head=None

    def search(self,key):
        ptr = self.head
        while ptr != None:
            if ptr.data == key.data:
                LinkedList.remove(self,key)
            else:
                LinkedList.add(self,key)
            ptr = ptr.next
    
    def add(self,nn):
        if self.head == None:
            self.head = nn
        elif nn.data < self.head.data:
            nn.next = self.head
            self.head = nn
        else:
            ptr = self.head
            follow = self.head
            while ptr.data < nn.data:
                follow = ptr
                ptr = ptr.next
            nn.next = ptr
            follow.next = nn
        return
    
    def remove(self,value):
        ptr = self.head
        if value.data == ptr.data:
            self.head = ptr.next
        else:
            follow = ptr
            while ptr != None:
                if ptr.data == value.data:
                    follow.next = ptr.next
                    print("element successfully removed")
                    break
                follow = ptr
                ptr = ptr.next
            print("element added successfully")
        return
            
                


    def display(self):
        elems=[]
        ptr = self.head
        while ptr.next is not  None:
            print(ptr.data.rstrip("\n\r"),'-->data')
            elems.append(ptr.data.rstrip("\n\r"))
            ptr=ptr.next
        print(elems,'-------->ele')
            

myll=LinkedList()
f = open('List.txt', 'r+')

for lines in f.readlines():
    line = lines.rstrip("\n\r")
    print(line)


f1 = open('List.txt', 'r+')
for lines in f1.readlines():
    obj=node(lines)
    myll.add(obj)
myll.display()

accept = input("Enter your element")
obj1 = node(accept)

# myll.search(obj1)
myll.display()

f.close()
f1.close()



# obj2 = node("bann")
# myll.add(obj2)
# #myll.display()
