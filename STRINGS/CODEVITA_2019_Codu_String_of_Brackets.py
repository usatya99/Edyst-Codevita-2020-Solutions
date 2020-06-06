string=input()
p=0
st=0
op=['(','{','[']
co=[')','}',']']
for i in range(len(string)):
    if string[i] in op:
        d={"{":"}","[":"]","(":")"}
        p+=1
        c=0
        l=[]
        for j in range(i+1,len(string)):
            if string[j]==d[string[i]] and len(l)==0:
                if c>=2:
                    st+=1
                break
            elif string[j] in op:
                l.append(string[j])
            elif string[j]=="*":
                c+=1
            elif string[j] in co:
                l.pop(-1)
            else:
                pass
        else:
            pass
if p==st:
    print("Yes",st)
else:
    print("No",st)
        




