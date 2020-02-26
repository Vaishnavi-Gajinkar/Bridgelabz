import toBinary
import PowerOfTwo
sw=toBinary.newL
arr=[]
if len(sw)<8:
    app=8-len(sw)
    for i in range(app):
        arr.append(0)
for j in range(len(sw)):
    arr.append(sw[j])
print(arr)

a1=arr[0:4]
a2=arr[4:8]
a=a2+a1
print(a)
dec=0
sum=0
for k in range(-1,-8,-1):
    dig=a[k]
    sum+=dig*pow(2,dec)
    dec+=1
print(sum)
if sum in PowerOfTwo.s:
    print("This is a power of two")
else:
    print("It is not a power of two")