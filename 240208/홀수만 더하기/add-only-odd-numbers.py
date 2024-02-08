n=int(input())
sum_value=0
for _ in range(n):
    num=int(input())
    if num%2==1 and num%3==0:
        sum_value+=num 
print(sum_value)