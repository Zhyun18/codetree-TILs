a,b=tuple(map(int,input().split()))
def solution(a,b):
    cnt=0
    for num in range(a,b+1):
        if num%2==0:
            continue
        elif num%10==5:
            continue 
        elif num%3==0 and num%9!=0:
            continue
        else:
            cnt+=1
    return cnt # for loop 을 다 돌아서 합산된 cnt 를 구하면 됨 
print(solution(a,b))