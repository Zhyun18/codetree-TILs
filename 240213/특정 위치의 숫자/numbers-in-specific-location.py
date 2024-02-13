arr=list(map(int,input().split()))
sum_value=0
for i in range(len(arr)):
    if i==2 or i==4 or i==9:
        sum_value+=arr[i] 
print(sum_value)