n=int(input())
def solution(n):
    num=1 # 주어진 함수에서 선언해야함
    for _ in range(n):
        for _ in range(n):
            print(num,end=' ')
            num+=1
            if num>9:
                num=1
        print()

solution(n)