from Dequeue import *

dq = DeQueue()

stri = input("Enter a string")
toChar = list(stri)
for i in toChar:
    dq.add_Rear(i)
print(toChar)
dq.show()
size = len(toChar)
sh = size / 2
j=0
flag = 1
if size%2 == 0:
    sh = size/2
else:
    sh = size/2 - 1

while j<=sh:
    front = dq.rem_Front()
    print(front,"removed", end=" ")
    rear = dq.remv_Rear()
    print(rear,"removed")
    dq.show()

    if front == rear:
        flag = 1
    else:
        flag = 0
        break

if flag == 1:
    print("String is palindrome")
else:
    print("String is not palindrome")


