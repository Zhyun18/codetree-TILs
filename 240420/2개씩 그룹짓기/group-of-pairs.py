n=int(input())
arr=list(map(int,input().split()))
arr=list(sorted(arr)) 

sum_value=[]
for i in range(len(arr)):
    sum_value.append(arr[i]+arr[2*n-i-1]) 
print(max(sum_value))