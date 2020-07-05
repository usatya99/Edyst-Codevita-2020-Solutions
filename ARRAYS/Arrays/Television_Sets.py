n=int(input())
r1,r2=map(int,input().split())
r=int(input())
cost,final=0,0
mon=[31,28,31,30,31,30,31,31,30,31,30,31]
l2=[]
for i in range(len(mon)):
    l1=[]
    for j in range(1,mon[i]+1):
        l1.append((6-(i+1))**2+abs(15-j))
    l2.append(l1)
for i in range(n+1):
    for j in l2:
        for k in j:
            if k>=n:
                ntv=n-i
                cost+=(r1*i+r2*ntv)
            else:
                ntv=n-i
                tv=k-ntv
                if(tv<0):
                    cost+=(r2*k)
                else:
                    cost+=(r1*tv+r2*ntv)
        final+=cost
        cost=0
    if final>=r:
        print(i)
        break
    else:
        final=0
else:
    print(n)
