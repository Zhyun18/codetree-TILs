#  정의된 함수 f 가 해당 함수를 구현하는 데 동일한 함수 f 를 다시 이용하게 되는 것 : 재귀함수 
n=int(input())

def solution(n):
    if n==0:
        return # 퇴각 
    solution(n-1)
    print('HelloWorld')

solution(n)