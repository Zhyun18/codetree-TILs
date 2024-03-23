n=int(input())

# n ~ 1 까지 1씩 감소하며 하나씩 출력했다가, 다시 1부터 N 까지 1씩 증가하며 증가 

def solution_1(n):
    if n==0:
        return 
    print(n,end=' ')
    solution_1(n-1)


solution_1(n)

def solution_2(n):
    if n==0:
        return 
    solution_2(n-1)
    print(n,end=' ')

solution_2(n)