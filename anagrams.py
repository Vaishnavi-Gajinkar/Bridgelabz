print("Enter 1st string")
s1=input()
s1=sorted(s1)
print("Enter 2nd string")
s2=input()
s2=sorted(s2)
if s1==s2:
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")