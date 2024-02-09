sum_value=0
cnt=0
avg_value=0
for _ in range(10):
    num=int(input())
    if 0<=num<=200:
        sum_value+=num
        cnt+=1
        avg_value=sum_value/cnt 
print(f'{sum_value} {avg_value:.1f}')