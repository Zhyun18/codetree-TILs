n=int(input())

# 1 부터 N 까지의 합 구하여 출력
def solution(n):
    if n==1:
        return 1 
    return solution(n-1) + n # 값 반환 해줘야함 

print(solution(n))