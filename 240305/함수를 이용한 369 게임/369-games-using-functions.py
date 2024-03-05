a,b=tuple(map(int,input().split()))
# 1) 3,6,9 중 하나가 들어가는 경우 
def solution(a,b):
    cnt=0
    for i in range(a,b+1):
        if ('3' in str(i) or '6' in str(i) or '9' in str(i)) and i%3!=0:
            cnt+=1
    return cnt

# 2) 3의 배수인 경우 
def solution2(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0:
           cnt+=1
    return cnt
print(solution(a,b)+solution2(a,b))