t=int(input())
for _ in range(t):
    Arr=[i for i in input().split()]
    digit,names=[],[]
    for i in Arr:
        if i.isdigit():
            digit.append(int(i))
        else:
            names.append(i.lower())
    digit.sort()
    names.sort()
    result=[]
    for i in range(len(names)):
        print(names[i],digit[i],end=' ')
    print()




