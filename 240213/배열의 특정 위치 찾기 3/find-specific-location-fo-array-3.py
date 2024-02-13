arr=list(map(int,input().split()))
cnt=0
sum_value=0

for i in range(len(arr)):
    if arr[i]==0:
        break
    cnt+=1

for i in range(cnt,cnt-3,-1):
    sum_value+=i 
print(sum_value)