import math
def f(n):
    a=list()
    while(n%2==0):
        a.append(2)
        n=n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            a.append(i)
            n=n//i
    if n>2:
        a.append(n)
    return a

try:
    n=int(input())
    if n>=0:
        arr=[0]*(n+1)
        for i in range(1,n+1):
            l=f(i)
            for j in l:
                arr[j]=arr[j]+1
        for i in range(n+1):
            if arr[i]!=0:
                print(arr[i],end=' ')
    else:
        print("Invalid Input")
except:
    print("Invalid Input")




