n=int(input())
cnt=0
for i in range(n):
    sum_val=0
    avg_val=0
    arr=list(map(int,input().split()))
    for j in arr:
        sum_val+=j
        avg_val=sum_val/4 
    if avg_val>=60:
        print('pass')
        cnt+=1
    else:
        print('fail')
print(cnt)