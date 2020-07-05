s=input().strip()
if(s[0]=='{' and s[len(s)-1]=='}' and s[1]==':'):
   if(s.find(',')):
       k=s.index(',')-1
       i=s.index('[')
       j=s.index(']')
       if(s[k]=='}' and s[len(s)-1]=='}' and s[i+1]=='{' and s[j-1]=='}'):
           print(1)
       else:
           print(-1)
   else:
       print(-1)
else:
   print(-1)


