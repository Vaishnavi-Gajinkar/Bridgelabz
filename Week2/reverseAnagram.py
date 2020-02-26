from Stack import *
class prime:

    def __init__(self):
        self.list = []                  

    def prime(self,r1,r2):
        lis= []                         #list to store the prime number the range r1 to r2
        for i in range(r1,r2+1):
            if prime.prime_check(self,i):
                lis.append(i)
        self.list.append(lis)
        return lis

    def Print(self,itr):                #printing the 2d array
        for i in range(itr):
            print(self.list[i])
    
    def prime_check(self,num):
        if num < 2:                     # if the num is < 2 its not a prime number
            return False
        if num == 2:                    # if the given num is 2 return true since 2 is a prime number
            return True
        count = 0                       #to count the divisors
        for i in range(2,(num//2)+1):
            if num%i == 0:
                count +=1
                return False
        if count == 0:
            return True

    def anagram(self,num):
        temp = 0
        while num >= 10:
            temp = (temp*10) + (num%10)
            num = num//10
        temp = (temp*10) + (num%10)
        return temp


pr = prime()
pus = stack()
nd = node()

num = []
for r in range(10,1001):
    if(pr.prime_check(r)):          #checking if number is prime
        ana = pr.anagram(r)         #reversing the number
        if(pr.prime_check(ana)):    #checking reversed string is prime
            num.append(r)           #adding number in list if true
print(num)

for i in num:
    n = node(i)                     #create object for each anagram
    pus.push(n)                     #push into stack

for j in range(len(num)):
    print(pus.pop(), end=" ")       #Pop data from stack
print()
    

