arr=list(map(int,input().split()))
cnt=0

for ele in arr:
    if ele==0:
        break
    cnt+=1

sum_val=0
ans_cnt=0
for i in range(cnt):
    if arr[i]%2==0:
        sum_val+=arr[i]
        ans_cnt+=1
print(ans_cnt,sum_val)