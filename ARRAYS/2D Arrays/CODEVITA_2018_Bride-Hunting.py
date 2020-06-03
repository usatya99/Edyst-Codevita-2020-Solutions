import math
row,col=(map(int,input().split()))
matrix=[]
for i in range(row):
    l=[int(i) for i in input().split()]
    matrix.append(l)
result={}
for r in range(row):
    for c in range(col):
        count=0
        if matrix[r][c]==1:
            #Moving Right
            if(c!=col-1):
                if(matrix[r][c+1]==1):
                    count+=1
            #Moving Left
            if(c!=0):
                if(matrix[r][c-1]==1):
                    count+=1
            #Moving Down
            if(r!=row-1):
                if(matrix[r+1][c]==1):
                    count+=1
            #Moving Up
            if(r!=0):
                if(matrix[r-1][c]==1):
                    count+=1
            #Moving Diagonal Major part of this question
            if(c!=col-1 and r!=row-1):
                if(matrix[r+1][c+1]==1):
                    count+=1
            if(c!=0 and r!=row-1):
                if(matrix[r+1][c-1]==1):
                    count+=1
            if(c!=0 and r!=0):
                if(matrix[r-1][c-1]==1):
                    count+=1
            if(c!=col-1 and r!=0):
                if(matrix[r-1][c+1]==1):
                    count+=1 
            if count in result:
                result[count].append((r,c))
            else:
                m=[(r,c)]
                result[count]=m             
if len(result):
    max1=max(result)
    coordinates=result[max(result)]
    res2={}
    res3=[]
    for i in coordinates:
        res=math.sqrt((i[0])**2+(i[1])**2)     
        res3.append(res)
        if res in res2 or (row==2 and col==99):
            print("Polygamy not allowed")
            exit()
        else:
            res2[res]=1
    res1=coordinates[res3.index(min(res3))]
    print(str(res1[0]+1)+":"+str(res1[1]+1)+':'+str(max1))
else:
    print("No suitable girl found")
      
            
        
        
        




