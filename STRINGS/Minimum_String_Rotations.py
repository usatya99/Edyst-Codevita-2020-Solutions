def solve(arr):
    n=len(arr[0])
    if all(arr[0]==i for i in arr):
        return 0
    else:
        d={(arr[0][i:]+arr[0][:i]): i for i in range(n)}
        for s in arr[1:]:
            if len(s)!=n:
                return -1
            for i in range(n):
                temp=s[i:]+s[:i]
                if temp not in d:
                     return -1
                d[temp]+=i
        return min(d.values())


t=int(input())
l=[]
for _ in range(t):
    c=input()
    l.append(c)
print(solve(l))

     
    




