a,b=map(int,input().split())
sum_value=0
if a>=b:
    for i in range(b,a+1): # step -1 으로 지정할 필요 x
        if i%5==0:
            sum_value+=i
else:
    for i in range(a,b):
        if i%5==0:
            sum_value+=i 
print(sum_value)