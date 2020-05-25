value=int(input())
#count the number of five rupee coin
five=int((value-4)/5)
#count the nimber of onr rupee coin 
if (value-five*5)%2==0: 
    one=2
else:
    one=1    
#counnt the number of two rupee coin
two=int((value-5*five-one)/2)
#print the required number
print(five+one+two,five,two,one)




