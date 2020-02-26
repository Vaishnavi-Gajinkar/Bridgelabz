import os

class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


class ll:
    def __init__(self):
        self.head=None

    def search(self,data):
        newnod=node(data)
        curr=self.head
        while curr.next != None:
            if curr.data == newnod.data:
                print("Item found")
                ll.remove(self,newnod.data)
                return True
            curr=curr.next
            
            return False
    
    def add(self,data):
        newnod=node(data)
        if self.head == None:
            self.head = newnod
        else:
            curr = self.head
            while curr.next != None:
                curr=curr.next
            newnod.next = curr.next
            curr.next=newnod
        
        
    def remove(self,data):
        curr=self.head
        prev=self.head
        while curr.data != data:
            prev=curr
            curr=curr.next
        prev.next=curr.next
        print("Item removed")
        ll.disp(self)
        
    def disp(self):
        curr=self.head
        while curr is not None:
            print(curr.data)
            curr=curr.next
        # print(curr.data)

    def size(self):                                 #count the number of elements in list
         sh = self.head                 
         count = 0
         while sh.next != None:
             count +=1
             sh = sh.next
         count +=1
         return count

    def element(self):
        ptr = self.head
        while ptr != None:
            f.write(" ",ptr.data)
        f.write(" ",ptr.data)
        

l = ll()
f = open('DataS.txt', 'r')                          # Open and read the file
file = f.read().split("\n")
f.close()
for i in file:
    print(i)
print()

print("Current elements in the list are")
l.disp()

for i in file:                              
    l.add(i)
word = input("Enter the word, to check")            #reading word from the user

result = l.search(word)                             #searching the element in list
print(result)

if result:
    l.remove(word)                                  #removing the word
    print("After Searching element in the list ")
    l.disp()
    print("element removed")
    
    f = open('DataS.txt', 'w')                      #Delete the word form the file by over writting.
    f.write('')
    f.close()
    length = l.size()
    f = open('DataS.txt', 'a+')
    l.element()
    f.close()
else:
    l.add(word)                                     #word not found hence adding it to end of list
    print("Updated elements are")
    l.disp()
    
    f = open('DataS.txt', 'a+')                     # adding the word to file
    f.write(word)
    f.close()