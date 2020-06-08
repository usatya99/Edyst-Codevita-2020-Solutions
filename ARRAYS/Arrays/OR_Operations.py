from itertools import combinations
import functools
t=int(input())
for _ in range(t):
    arr=list(set([int(i) for i in input().split()][1:]))
    s=0
    for i in arr:
        s=s|i
    for i in range(1,len(arr)+1):
        res=combinations(arr,i)
        c=0
        for j in res:
            z=functools.reduce(lambda x,y : x|y , j)
            if z==s:
                c=1
                print(i)
                break
        if c==1:
            break
    if c==0:
        print(0)
        









