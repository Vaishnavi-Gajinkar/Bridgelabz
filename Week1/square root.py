print("Enter a value to find its squareroot")
c=int(input())
t=c
ct=c/t
e=pow(10,-15)
while abs(t-ct)>(e*t):
    t=((c/t)+t)/2
    ct=c/t
print(t)
