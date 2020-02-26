from Dequeue import *

do = True
deq= DeQueue()
print("<-------Enter your choice------>\n1 - enter front\n2 - delete front\n3 - enter rear\n4 - delete rear\n5 - Show elements\n6 - Count elements")
while do == True:
    choice = int(input())
    if choice == 1:
        ans = input("Enter value")
        deq.add_Front(ans)
    elif choice == 2:
        deq.rem_Front()
    elif choice == 3:
        ans = input("Enter value")
        deq.add_Rear(ans)
    elif choice == 4:
        deq.remv_Rear()
    elif choice == 5:
        deq.show()
    elif choice == 6:
        deq.count()
    ans = input("Do you wish to continue?\nEnter your choice if yes")
    if ans.casefold() in 'y,yes':
        do = True
    else:
        do = False
    
