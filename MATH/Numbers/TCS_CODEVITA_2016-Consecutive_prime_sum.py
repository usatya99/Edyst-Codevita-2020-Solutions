def isprime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return 0
        return 1
    return 0
l=[]
l1=[]
for i in range(2,1000):
    for j in range(2,i): 
        if i%j==0:
            break
    else:
        l.append(i)
    if isprime(sum(l)):
        l1.append(sum(l))
l1=list(set(l1))
t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    for i in range(3,n+1):
        if i in l1:
            c+=1
    print(c)
      
            
        




