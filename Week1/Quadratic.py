import math
print('Enter values of a, b,c for the quadratic equation : ax2+bx+c')
while(True):
    print('enter a')
    a=float(input())
    print('enter b')
    b=float(input())
    print('enter c')
    c=float(input())
    try:
        d=pow(b,2)
        print(d)
        de=d-4*a*c
        print(de)
        sq=math.sqrt(de)
        r1=(-b+sq)/2*a
        r2=(-b-sq)/2*a
    except:
        print("Enter valid values ")
        continue
        
print(r1)
print(r2)
