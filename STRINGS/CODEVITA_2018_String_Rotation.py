
#used to check whether the two strings are equal or not
def Result(s1,s2):
    for i in s1:
        if i not in s2 or s1[i]!=s2[i]:
            return False
    return True


#making each character frequency updated in the count
def getCharcount(s):
    count=dict()
    for i in s:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

#function to check the strings are anagram or not
def isAnagram(string1,string2):
    if len(string1)<len(string2):
        return False
    count2=getCharcount(string2)
    for i in range(0,len(string1)-len(string2)+1):
        window=string1[i:i+len(string2)]
        countwindow=getCharcount(window)
        if Result(count2,countwindow):
            return True
    return False  
    
string=input()
t=int(input())
startchars=0
startchar=[]
for _ in range(t):
    direaction,val=(map(str,input().split()))
    val=int(val)
    if direaction=='L':
        startchars=(startchars+val)%len(string)
    else:
        startchars=(startchars-val)%len(string)
    startchar.append(string[startchars])
if isAnagram(string,startchar):
    print("YES")
else:
    print("NO")
    




