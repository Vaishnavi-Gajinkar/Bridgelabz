print("Enter temperature")
temp=float(input())
print("is this in celcius or fahrenheit")
ans=input()
if ans=='celcius' or ans=='c':
    op=(temp*9/5)+32
    print(op,"F")
elif ans[0]=='f'.casefold():
    op=(temp-32)*5/9
    print(op,"C")
else:
    pass


