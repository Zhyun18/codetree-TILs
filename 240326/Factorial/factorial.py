n=int(input())

def solution(n):
    if n==1:
        return 1
    return solution(n-1)*n

print(solution(n))