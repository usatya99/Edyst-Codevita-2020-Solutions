t=int(input())
for _ in range(t):
    n,mod=(map(int,input(). split()))
    arr1=[int(i) for i in input().split()]
    arr2=[int(i) for i in input().split()]
    sample_sum=0
    for i in range(n):
        sample_sum=sample_sum+(arr1[i]*arr2[i])
    original_sum=sample_sum
    for j in range(n):
        s=arr1[j]*arr2[j]
        z=min((arr1[j]-2*mod)*arr2[j] , (arr1[j]+2*mod)*arr2[j])
        temp_sum=sample_sum-s+z
        if temp_sum<original_sum:
            original_sum=temp_sum
    print(original_sum)
        
        
    
        




