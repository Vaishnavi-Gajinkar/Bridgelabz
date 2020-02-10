print('Enter values of a, b,c for the quadratic equation : ax2+bx+c')
print('enter a')
a=int(input())
print('enter b')
b=int(input())
print('enter c')
c=int(input())
del=math.pow(b,2)-2*a*c
sq=math.sqrt(del)
r1=(-b+sq)/2*a
r2=(-b-sq)/2*a