#matrix rotation without extra space...!
def rotateMatrix(A,n):
    for i in range(n//2):
        for j in range(i,n-i-1):
            temp=A[i][j]
            A[i][j]=A[n-1-j][i]
            A[n-1-j][i]=A[n-1-i][n-1-j]
            A[n-1-i][n-1-j]=A[j][n-1-i]
            A[j][n-1-i]=temp
    return A
    
n=int(input())
matrix=[]
for i in range(n):
    mat1=[int(i) for i in input().split()]
    matrix.append(mat1)
#Read the values fo matrix in Matrix form

while(True):
    query=[i for i in input().split()]
    if query[0]=='A':
        for i in range(int(query[1])//90):
            matrix=rotateMatrix(matrix,n)
           # always updating the values of the matrix
    elif query[0]=='Q':
        print(matrix[int(query[1])-1][int(query[2])-1])
    elif query[0]=='U':
        matrix[int(query[1])-1][int(query[2])-1]=int(query[3])
    else:
        exit()
        
    




