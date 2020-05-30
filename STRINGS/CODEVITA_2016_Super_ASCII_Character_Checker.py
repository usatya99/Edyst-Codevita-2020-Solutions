alpha="abcdefghijklmnopqrstuvwxyz"
dictalpha={}
for i,j in enumerate(alpha):
    dictalpha[j]=i+1
t=int(input ())
for f in range(t):
    string=input().rstrip()
    dict1={}
    for i in string:
        if i not in dict1:
            dict1[i]=1
        else:
            dict1[i]+=1
    for k,v in dict1.items():
        if dictalpha[k]==v:
            c=0
        else:
            c=1
            break
    if c==0:
        print('Yes')
    else:
        print('No')
        
    
       



