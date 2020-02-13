l=[]
n=1000
for i in range(1, n+1):
    temp=0
    for j in range(2,i):
        if (i%j == 0):
            temp+=1
    if(temp==2):
        l.append(i)     
print(l)
