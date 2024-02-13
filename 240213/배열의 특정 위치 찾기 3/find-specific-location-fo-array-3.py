arr=list(map(int,input().split()))
cnt=0
sum_value=0

for i in range(len(arr)):
    if arr[i]==0:
        break
    cnt+=1


for i in range(cnt-1,cnt-4,-1):
    sum_value+=arr[i] 
print(sum_value)