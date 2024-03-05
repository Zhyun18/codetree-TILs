n=int(input())
def solution(n):
    sum_value=0
    for i in range(1,n+1):
        sum_value+=i 
    return sum_value//10

print(solution(n)) # 반환 값을 출력하려면 출력하는 코드를 따로 작성해야함