a,b=input().split()
num=int(b)
arr=list(a)
arr.sort()
largest=int("".join(arr[::-1]))
if(num>largest):
    print(-1)
else:
    num=num+1
    while(sorted(list(str(num)))!=arr):
        num+=1
    print(num)




