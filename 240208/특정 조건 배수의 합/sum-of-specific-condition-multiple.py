a,b=map(int,input().split())
sum_value=0
for n in range(a,b+1):
    if n%5==0:
        sum_value+=n 
print(sum_value)