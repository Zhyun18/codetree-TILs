n=int(input())
def solution(n):
    if n==1:
        return 1 
    if n==2:
        return 2
    if n%2==1:
        return solution(n-2)+n 
    else:
        return solution(n-2)+n 

print(solution(n))