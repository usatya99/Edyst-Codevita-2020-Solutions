def solve(n):
    l=[0]*(n+1)
    l[0]=1
    l[1]=0
    l[2]=1
    for i in range(2,n+1):
        l[i]=((i-1)*(l[i-1]+l[i-2]))%1000000007
    return l[n]%1000000007
n=int(input())
print(solve(n))




