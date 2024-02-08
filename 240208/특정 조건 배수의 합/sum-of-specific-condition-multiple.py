a,b=map(int,input().split())
sum_value=0
if b>=a: # a,b 의 대소 비교 케바케
    for n in range(a,b+1):
        if n%5==0:
            sum_value+=n
else:
    for n in range(b,a-1,-1):
        if n%5 == 0:
            sum_value+=n  
print(sum_value)