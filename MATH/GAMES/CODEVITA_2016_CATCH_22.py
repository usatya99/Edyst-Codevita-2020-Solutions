n=int(input())
for i in range(0,n):
    f,b,t,fd,bd=map(int,input().split())
    dist=0
    ans=0
    forward=0
    backward=0
    bd=(-1)*bd
    if(f==b and fd>f):
        print("No Ditch")
    else:
        while(True):
            dist=dist+f
            ans=ans+f
            if(dist>=fd):
                forward=1
                break
            dist=dist-b
            ans=ans+b
            if(dist<=bd):
                backward=1
                break
        if(forward==1):
            if(dist==fd):
                t=t*ans
            else:
                ans=ans-(dist-fd)
                t=t*ans
            print(t,"F")
        if(backward==1):
            if(dist==bd):
                t=t*ans
            else:
                ans=ans+(dist-bd)
                t=t*ans
            print(t,"B")
