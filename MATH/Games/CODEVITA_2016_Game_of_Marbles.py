import math

def findlcm(a):
    try:
        a=[int(i) for i in a]
        lcm=a[0]
        
        for i in a[1:]:
            if i >= 1 and i<=100:
                lcm=int(lcm * i) / int(math.gcd(lcm,i))
                lcm=int(lcm) 
            else:
                lcm=0
        return lcm
    except:
        return None

n=int(input())



points={"Darrell":0,"Sally":0}

questions={}
flag=0
c=0
members={"Darrell":"Sally","Sally":"Darrell"}

for _ in range(n):
    line=input().split()
    if line[0]=="A":
        if questions[members[line[1]]]==None:
            print("Invalid Input")
            break
        else:
            if c==0:
                firstanswered=line[1]
                c=1
            grouplist=questions[members[line[1]]].split(",")
            
            crct_answer=findlcm(grouplist)
            
            if crct_answer==None or crct_answer==0:
                print("Invalid Input")
                break
            print(members[line[1]]+"'s question is :",questions[members[line[1]]])

            if line[2] == str(crct_answer):
                print("Correct Answer")
                points[line[1]]+=10
                print("{}: 10points".format(line[1]))
            elif line[2]=="PASS":
                print("Question is PASSed")
                print("Answer is:",crct_answer)
                print("{}: 0points".format(line[1]))
            else:
                print("Incorrect Answer")
                print("{}: 0points".format(line[1]))
            questions[members[line[1]]]=None
    else:
        try:
            if "," in line[1]:
                questions[line[0]] = line[1]
                if flag==0:
                    firstquestioned=line[0]
                    flag=1
            else:
                raise Exception
        except:
            print("Invalid Input")
            break
else:
        print("Total Points:")
        if firstquestioned == "Darrell":
            print("Darrell: {}points".format(points["Darrell"]))
        else:
            print("Sally: {}points".format(points["Sally"]))
        if firstanswered=="Darrell":
            print("Darrell: {}points".format(points["Darrell"]))
        else:
            print("Sally: {}points".format(points["Sally"]))
        if points["Darrell"] == points["Sally"]:
            print("Game Result: Draw")
        else:
            print("Game Result: {} is winner".format(max(points,key=points.get)))
