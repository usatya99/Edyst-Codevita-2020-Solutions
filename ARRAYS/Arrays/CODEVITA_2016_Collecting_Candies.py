from queue import PriorityQueue
T=int(input())
for i in range(T):
    n=int(input())
    l=list(map(int,input().split()))
    s=PriorityQueue()
    for i in l:
        s.put(i)
    sum1=0
    while(s.qsize()!=1):
        s1=s.get()+s.get()
        sum1+=s1
        s.put(s1)
    print(sum1)
        
        
