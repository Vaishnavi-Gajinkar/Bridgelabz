str=input("Enter the input")
list=str.split(" ")
print(list)
li=[]
for i in range(1,len(list)):
    a=list[i]
    j=i-1
    while j>=0 and list[j]>a:
        list[j+1]=list[j]
        j-=1
    list[j+1]=a
    
print(list)