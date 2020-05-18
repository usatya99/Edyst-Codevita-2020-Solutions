try:
    b,n=(map(int,input().split()))
    l=[int(i) for i in input().split()]
except:
    print("Invalid Input")
else:
    l.sort()
    for i in l:
        if b>i:
            b-=i
        else:
            print("NO")
            break
    else:
        print("YES")
       



