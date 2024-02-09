n=int(input())
sum_value=0
avg_value=0
for _ in range(n):
    num=int(input())
    sum_value+=num
    avg_value=sum_value/n 
print(f'{sum_value} {avg_value:.1f}')