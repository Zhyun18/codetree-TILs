n=int(input())
def solution(n):
    cnt=0
    if n==1: 
        return cnt 
    if n%2==0:
        cnt+=1
        return solution(n//2) + cnt
    else:
        cnt+=1 
        return solution(n//3) + cnt


print(solution(n))