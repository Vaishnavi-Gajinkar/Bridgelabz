from Queue import *
        
do = True
que = Queue()
total_money = 10000
while do == True:
    print("<----------Select your choice------------>")
    print("1 - Check amount with cashier")
    print("2 - Deposit amount")
    print("3 - Withdraw amount")
    print("4 - Show queue")
    print("5 - Add a person to Queue")
    choice = int(input("6 - Remove the first person from Queue"))

    

    if choice == 1:
        print("Remaining balance is ",total_money)
    elif choice == 2:
        amt = int(input("Enter the amt to deposit"))
        total_money = total_money + amt
        que.deq()
    elif choice ==3:
        amt = int(input("Enter amt to withdraw"))
        total_money = total_money - amt
        que.deq()
    elif choice == 4:
        que.show()
    elif choice == 5:
        id = int(input("Enter ID of person"))
        que.enq(id)
        print("User added")
        que.show()
    elif choice == 6:
        que.deq()
        print("User removed")
        que.show()
    else:
        print("Invalid choice")
    ans = input("Do you wish to continue?")
    if ans.casefold() in 'y,yes':
        do = True
    else:
        do = False

