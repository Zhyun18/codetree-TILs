arr=list(map(int,input().split()))
sum_value=0
sum_value2=0
avg=0
cnt=0
for i in range(1,11):
    if i%2==0:
        sum_value+=arr[i-1]
        
    if i%3==0:
        sum_value2+=arr[i-1] 
        cnt+=1
        avg=sum_value2/cnt
print(f'{sum_value} {avg:.1f}')