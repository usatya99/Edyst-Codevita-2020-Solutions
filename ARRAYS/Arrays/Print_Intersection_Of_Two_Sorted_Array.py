t=int(input())

for i in range(t):

    n1=set(list(map(int,input().split()))[1:])

    n2=set(list(map(int,input().split()))[1:])

    l=sorted(n1.intersection(n2))

    for i in l:

        print(i,end=" ")

    print()




