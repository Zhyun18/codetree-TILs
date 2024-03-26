# 정수 n 
n=int(input())

# n 개의 정수 
arr=list(map(int,input().split()))

# 재귀함수 호출 
def solution(n):
    if n==0:
        return arr[0]
    return max(solution(n-1),arr[n-1]) 

print(solution(n-1))