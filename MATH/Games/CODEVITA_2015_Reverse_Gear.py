h=int(input())
for _ in range(h):
    f,b,t,d=[int(i) for i in input().split()]
    sdist=b+f
    sdisp=b-f
    step=(d-b)//sdisp
    if((d-b)%sdisp!=0):
        step+=1
    rd=d-(step*sdisp)
    tot=(step*sdist)+rd
    tt=tot*t
    print(tt)

