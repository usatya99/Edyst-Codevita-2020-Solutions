import math
n=int(input())
for _ in range(n):
    x=int(input())
    y=int(input())
    va=int(input())
    vb=int(input())
    min1=math.sqrt(x*x+y*y)
    while(x>=0 or y>=0):
        x-=va
        y-=vb
        d=math.sqrt(x*x+y*y)
        if d<min1:
            min1=d
    if min1==0.0:
        print("0.0")
    else:
        print ("{0:.4f}".format(min1)) 



