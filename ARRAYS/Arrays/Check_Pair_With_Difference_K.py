def checkpair(arr,size,k):
    i,j=0,1
    while(i<size and j<size):
        if arr[j]-arr[i]==k and i!=j:
            return 1
        elif arr[j]-arr[i]<k:
            j+=1
        else:
            i+=1
    return 0
    


t=int(input ())
for _ in range(t):
    l=[int(i) for i in input().split()]
    l=l[1:]
    k=int(input())
    size=len(l)
    if checkpair(l,size,k):
        print(1)
    else:
        print(0)
     
            



