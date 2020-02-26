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
    
print("range is 0 to 1000")
obj = prime()                   #creating object

itr = 0                         # an iterator variable to count the loop iterations
list = []                       # creating an empty list to store the prime numbers in the given range
for i in range(0,1000,100):
    lis = obj.prime(i,i+100)    # calling the prime function to get the prime numbers
    itr +=1
    list.append(lis)
obj.Print(itr)                  # printing the 2d prime number array