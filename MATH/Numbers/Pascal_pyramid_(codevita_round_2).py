from itertools import permutations
def solve(l):
    if len(l)==2:
        return l[0]*l[1]
    else:
        c=[]
        for i in range(len(l)-1):
            c.append(l[i]+l[i+1])
        return solve(c)
n=int(input())
l=[int(i) for i in input().split()]
l.sort()
l=l[-6:]
b=permutations(l)
m=[]
for i in b:
    c=solve(i)
    m.append(c)
print(max(m))
            
        




