n=int(input())

# 재귀함수 두개, 첫 번째 재귀함수 이용 1~N까지 출력 
def solution_one(n):
    if n==0:
        return  
    solution_one(n-1)
    print(n,end=' ')

solution_one(n)
print()

# 두 번째 재귀 함수, N~1 까지 출력
def solution_two(n):
    if n==0:
        return 
    print(n,end=' ')
    solution_two(n-1)

solution_two(n)