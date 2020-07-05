def s(x,y,a,b):
    return abs(x-a)+abs(y-b)
def dis(x,a,b):
   # print(x)
    x1,y1=x[0],x[1]
    x2,y2=x[2],x[3]
    x3,y3=(x1+x2+y2-y1)//2, (y1+y2+x1-x2)//2
    x4,y4=(x1+x2+y1-y2)//2, (y1+y2+x2-x1)//2
    return min(s(x2,y2,a,b),s(x1,y1,a,b),s(x3,y3,a,b),s(x4,y4,a,b))
t=int(input())
x=[]
for i in range(t):
    x1,y1,x2,y2=(map(int,input().split()))
    x.append([x1,y1,x2,y2,i+1])
a,b=(map(int,input().split()))
x.sort(key=lambda m : dis(m,a,b))
for i in range(t):
    print(x[i][4],end=' ')
    
    
    





