import math
print("enter values for P,N,R")
P=float(input())
Y=int(input())
R=float(input())
r=R/(12*100)
n=12*Y
payment=P*r/(1-pow(1+r,-n))
print("Monthly payments is ",payment)