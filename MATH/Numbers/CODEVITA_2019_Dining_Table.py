def fact(n): 
    factorial=[1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,6227020800,87178291200,1307674368000,20922789888000,355687428096000,6402373705728000,121645100408832000, 2432902008176640000]
    return factorial[n]

def ncr(n,r):
    if r==1:
        return n
    elif r==n or r==0:
        return 1
    else:
        result=fact(n)//fact(r)
        result=result//fact(n-r)
    return result 
t=int(input())
for _ in range(t):
    r,n=(map(int,input().split()))
    initial=n//r
    extra=n%r
    type_1=initial+1
    type_2=initial
    count=1
    for i in range(0,extra):
        count=count*ncr(n,type_1)
        n=n-type_1
    for i in range(extra,r):
        count=count*ncr(n,type_2)
        n=n-type_2
    print(count)
    





