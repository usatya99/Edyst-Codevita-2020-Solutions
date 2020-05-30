t=int(input())
for _ in range(t):
    String=input()
    Pstring=input()
    dict1={}
    for i in Pstring:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i]=1
        Pstring=set(Pstring)
    for i in String:
        if i in Pstring:
            print(i*dict1[i],end='')
    print()



