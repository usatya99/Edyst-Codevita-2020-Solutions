N=int(input())
#N=5
chakra=[[0 for i in range(N)] for i in range(N)]
ppoints=1+(N**2//11)
co=1
ppDict={1:(0,0)}
for i in range(N//2):
    row,col=i,i
    end_col=N-i-1
    while(col<end_col):#printing first row
        chakra[row][col]=co
        if co%11==0:
            ppDict[co]=(row,col)
        co+=1
        col+=1
    end_row=N-i-1
    while(row<end_row):#printing the last column
        chakra[row][col]=co
        if co%11==0:
            ppDict[co]=(row,col)
        co+=1       
        row+=1
    end_col=i
    while(col>end_col):#printing the bottom row
        chakra[row][col]=co
        if co%11==0:
            ppDict[co]=(row,col)
        co+=1
        col-=1
    end_row=i
    while(row>end_row):#printing the first column
        chakra[row][col]=co
        if co%11==0:
            ppDict[co]=(row,col)
        co+=1
        row-=1
if N%2==1:
    chakra[N//2][N//2]=N*N
for i in range(N):
    for j in range(N):
        print(str(chakra[i][j]),end='\t')
    print()
print("Total Power points :",ppoints)
for i in ppDict.values():
    print("("+str(i[0])+","+str(i[1])+")")




