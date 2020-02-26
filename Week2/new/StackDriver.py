from Stack import *

mystk = stack()
exp = input("Enter an expression")
l = list(exp)
print(l)
puc=0
poc=0
flag = 0
for i in l:
    if i in '{,[,(':
        n = node(i)
        mystk.push(n)
        puc += 1
        print(mystk.size_of())
       
        if i=='(':
            if ')' in l:
                sktop = mystk.pop()
                # +poc +=1

        if i == '{':
            if '}' in l:
                sktop = mystk.pop()
                # +poc += 1
        if i == '[':

            if ']' in l:
                sktop = mystk.pop()
                # +poc += 1

print(mystk.size_of(),'------->last')

print(puc)
print(poc)
if mystk.size_of() == 0:
    print("Balanced parentheses expression")