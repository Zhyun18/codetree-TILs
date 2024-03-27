n=int(input())
def solution(n):
    if n==1:
        return 0

    if n%2==0:
        return solution(n//2)+1
    else:
        return solution(n*3+1)+1

print(solution(n))