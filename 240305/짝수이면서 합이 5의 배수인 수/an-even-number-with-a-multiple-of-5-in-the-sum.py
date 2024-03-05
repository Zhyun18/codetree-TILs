n=int(input())
def solution(n):
    if n%2==0 and ((n//10)+(n-(n//10)*10))%5==0:
        return 'Yes'
    else:
        return 'No'

print(solution(n))