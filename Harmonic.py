print("Enter the value of N")
n=int(input())
sum=0
for i in range(1,n):
    sum+=1/i
print("Value of Harmonic series till",n,"is",sum)