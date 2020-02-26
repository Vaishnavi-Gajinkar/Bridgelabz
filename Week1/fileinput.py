print("Enter number of Fruits to add")
n=int(input())
l=[]
f= open("List.txt",'w+')
print("Enter names of fruits")
for i in range(n):
    l.append(input())
l.sort()
for j in range(len(l)):
    f.write(str(l[j]))
    
f.write(l[-1])
f1= open("List.txt",'r')
f1.read()