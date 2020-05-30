import math
def EMI(loanAmt,monthIrate,noofyrs):
    deno=1-(1/math.pow((1+monthIrate),noofyrs*12))
    numo=loanAmt*monthIrate
    result=numo/deno
    #print(result)
    return result
t=int(input())
for _ in range(t):
    bank=[0]*2
    roi=[0]*2
    Principal=int(input())
    Years=int(input())
    for i in range(2):
        bank[i]=0
        roi[i]=0
        slabs=int(input())
        for _ in range(slabs):
            sample=[i for i in input().split()]
            slabs_roI,slabs_Time=int(sample[0]),float(sample[1])
            #print(slabs_Time)
            roi[i]+=slabs_Time
            bank[i]+=EMI(Principal,slabs_roI,slabs_Time)
    #print(bank)
  #  print(roi)
    if bank[0]<bank[1] or roi[0]>roi[1]:
        print("Bank B")
    else:
        print("Bank A")
            
        
    
    




