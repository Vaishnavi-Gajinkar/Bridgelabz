class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        ptr = self.top
        if self.top is None:
            # print(value.data)
            self.top = value
            self.count +=1
        else:
            # print(value.data)
            value.next = self.top
            self.top = value
            self.count +=1

    def pop(self):

        result=0
        if self.top is None:
            print("Stack empty! Nothing to pop")
        elif self.top.next == None:
            self.top = None
            self.count -=1
        else:
            result = self.top.data
            self.top = self.top.next
            self.count -=1
        return result
        

    def peek(self):
        if self.top is None:
            return print("Stack Empty")
        else:
            return print(self.top.data)

    def is_Empty(self):
        if self.top is None:
            return True
        else:
            return False

    def size_of(self):
        return self.count

