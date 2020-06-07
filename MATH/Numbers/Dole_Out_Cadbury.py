def solve(a,b):
    min1=min(a,b)
    max1=max(a,b)
    if min1==0:
        return 0
    if min1==1:
        return b*a
    r=max1//min1
    s=max1%min1
    r=r+solve(s,min1)
    return r

T=int(input())
for _ in range(T):
    P,Q,R,S=(map(int,input().split()))
    ans=0
    for i in range(P,Q+1):
        for j in range(R,S+1):
            ans+=solve(i,j)
    print(ans)




