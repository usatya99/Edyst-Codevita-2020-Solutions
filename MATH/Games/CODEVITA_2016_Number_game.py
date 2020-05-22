import math
def solve(n):
    s=[]
    while(n%2==0):
        s.append(2)
        n=n//2
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            s.append(i)
            n=n//i
    if(n>2):
        s.append(n)
    return s
t=int(input())
input1=[int(i) for i in input().split()]
sum1=0
for i in input1:
    l=list()
    l=solve(i)
    for j in l:
        sum1=sum1^j
#print(sum1)
if(sum1==0):
    print("JASBIR")
else:
    print("AMAN")
