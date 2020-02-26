def swap(part,s,e):
    part=""
    char = list(part.split(""))
    temp=char[s]
    char[s]=char[e]
    char[e]=temp
    return(part.join(char))
def permute(var,l,r):
    if l==r:
        print(var)
    else:
        for i in range(l,r,1):
            res=swap(var,l,i)
            permute(res,l+1,r)
s="a"
permute(s,0,len(s))