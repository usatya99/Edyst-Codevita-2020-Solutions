n=int(input())
brides_to_be,groomes_to_be=(map(str,input().split()))
def leftRotate(str1):
    return str1[1:]+str1[0]
j,i,f=0,0,1
while(i<n and len(groomes_to_be)!=0 ):
    while(len(brides_to_be)!=0):
        #print(i,j)
        #print(brides_to_be,groomes_to_be)
        if brides_to_be[i]==groomes_to_be[j]:
            brides_to_be=brides_to_be[1:]
            groomes_to_be=groomes_to_be[1:]
            #print(brides_to_be,groomes_to_be)
        elif brides_to_be[i] not in groomes_to_be:
            f=1
            break
        else:
            groomes_to_be=leftRotate(groomes_to_be)
            #print(groomes_to_be)
            j=0
    if(f==1):
        break
    i+=1
print(len(groomes_to_be),end='')
        
