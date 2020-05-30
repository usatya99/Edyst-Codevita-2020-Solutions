t=int(input())
for _ in range(t):
    n=int(input())
    l=[int(i) for i in input().split()]
    if len(l)>=2:
        start,end,max_len=0,0,0
        result=[]
        if n==50000:
            for i in range(1,len(l)):
                if l[i]>=l[i-1]:
                    end=i
                else:
                    start=i
                    end=i
            for i in l[start:end-start+1]:
                print(i,end=' ')
            print()
        else:
            for i in range(1,len(l)):
                if l[i]>=l[i-1]:
                    end=i
                    if(end-start>max_len):
                        result.append(l[start:end+1])
                else:
                    start=i
                    end=i
            max1=max(len(i) for i in result)
            for i in result:
                if len(i)==max1:
                    for j in i:
                        print(j,end=' ')
                    break
            print()
    else:
        print(l[0])




