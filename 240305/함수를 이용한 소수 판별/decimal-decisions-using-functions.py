a,b=tuple(map(int,input().split()))
def solution(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    return n # 위치 

sum_value=0
for i in range(a,b+1):
    if i==1:
        sum_value=0
    else:
        sum_value+=solution(i)
print(sum_value)