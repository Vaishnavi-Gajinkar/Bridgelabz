def Binary(a,n,key):
    l=0
    r=n
    while(l<r):
        mid=(l+r)//2
        if key==a[mid]:
            return mid
        elif(key<a[mid]):
            r=mid-1
        else:
            l=mid+1
    return -1

# f=open("List.txt",'r')
# data = f.readline()
# l=[i.strip() for i in data.split(',')]
# f.close()
data=['kiwi','banana','apple','orange','fig']
data=sorted(data)
print(data)

key=input("enter name:")
print(key)
pos=Binary(data,len(data),key)
if pos==-1:
    print("Element not present in array")
else:
    print("Element found at position ",pos)
