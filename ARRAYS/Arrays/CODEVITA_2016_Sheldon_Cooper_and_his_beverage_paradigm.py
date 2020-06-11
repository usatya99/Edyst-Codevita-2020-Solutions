def solve(a,arr):
    l=0
    r=len(arr)-1
    while(l<r):
        if arr[l]+arr[r]==a:
            return True
        elif arr[l]+arr[r]>a:
            r-=1
        else:
            l+=1
    return False
t=int(input())
array=[]
for _ in range(t):
    array.append(int(input()))
X=int(input())
array.sort()
sum1=0
#print(array)
for i in range(t):
    if i>0 and array[i]==array[i-1]:
        continue
    a=X-array[i]
    #print(array[i+1:]+array[:i],a)
    if solve(a,array[:i]+array[i+1:]):
        print("True")
        break    
else:
    print("False")
            
            
   




