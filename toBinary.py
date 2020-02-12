print("Enter a decimal value")
val=int(input())
l=[]
i = 0
while val>=1:
    rem=val%2
    l.append(rem)
    val=val//2

newL=l[::-1]
for k in newL:
    print(k,end="")
print("")

#s=[str(i) for i in newL] 
#str=int("".join(s))
#res = int("".join(map(str, newL)))
#print(res)