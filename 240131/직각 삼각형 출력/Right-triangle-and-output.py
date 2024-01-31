# 입력값
n=int(input())

# 총 출력 줄 
for i in range(n):
    # 한 줄에 출력할 별 반복 
    for j in range(0,2*i+1):
        print('*',end='')
    print()