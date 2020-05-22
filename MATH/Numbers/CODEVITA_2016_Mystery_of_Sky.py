from datetime import date


class Date:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y

monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

weekdays={"Saturday":0,"Sunday":1,"Monday":2,"Tuesday":3,"Wednesday":4,"Thursday":5,"Friday":6}

def calculatestars(day,cur_date):
    crday=list(cur_date.split("/"))
    crday[2]=int(crday[2])
    crday[1]=int(crday[1])
    crday[0]=int(crday[0])
    if cur_date==None:
        return None
    else:
        
        if crday[0]<=31:
            noofdays=calculate_no_of_days("01/01/0001",cur_date)
        else:
            return None
        if crday[1]==2 and crday[0]>29:
            return None 
        if crday[1]==2 and crday[0]==29 and (crday[2]%4!=0 or crday[2]%400!=0):
            return None
        if noofdays % 4 ==3:
            return 0
        elif (weekdays[day]+noofdays)%7==0 or (weekdays[day]+noofdays)%7==1:
            return 0
        else:
            days=sum(monthdays[0:(crday[1]-1)])
            
            if crday[2]%4==0 and crday[2]%400==0 and crday[2]%200!=0:
                days-=1
            days+=crday[0]
            
            
            return min(days,50)

        
    
def countleapyears(dt):
    years=dt.y
    
    if dt.m<=2:
        years-=1
    return int(years/4-years/100+years/400)
        
def calculate_no_of_days(startdate,enddate):
    startlist=list(startdate.split("/"))
    endlist=list(enddate.split("/"))
    for i in range(3):
        startlist[i]=int(startlist[i])
        endlist[i]=int(endlist[i])
    
    date1=Date(startlist[0],startlist[1],startlist[2])
    
    date2=Date(endlist[0],endlist[1],endlist[2])
    
    n1=date1.y * 365 +date1.d
    
    for i in range(0,date1.m-1):
        n1+=monthdays[i]
        
    n1+=countleapyears(date1)
    
    n2=date2.y * 365 +date2.d
    
    for i in range(0,date2.m-1):
        n2+=monthdays[i]
        
    n2+=countleapyears(date2)
    return (n2-n1)
        
        
try:       
    day=input()
    date=input()
    ans=calculatestars(day,date)
    if ans==None:
        print("Invalid Date")
    else:
        print(ans)
except EOFError:
    print("Invalid Day")
