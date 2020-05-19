import math 
#To check prime number or not
def is_prime(n): 
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True
#To check happy number or not
def isHappy(n):
    sum1=0
    while(n):
        sum1+=(n%10)**2
        n=n//10
    if sum1==1 or sum1==10:
        return True
    if sum1==4:
        return False
    return isHappy(sum1)            
try:
    xlimit=int(input())
    ylimit=int(input())
    nth=int(input())
except:
    print("Invalid Input")
else:
    sum2=0
    for i in range(xlimit,ylimit+1):
        if is_prime(i) and isHappy(i):
            sum2+=1
        if sum2==nth:
            print(i)
            break
    else:
        print('No number is present at this index')
    




