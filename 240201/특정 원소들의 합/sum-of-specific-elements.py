# 4*4 2차원 배열 생성
arr=[list(map(int,input().split())) for _ in range(4)]
result=0
# 색칠 칸의 정수의합
for i in range(4):
    for j in range(i+1):
        result+=arr[i][j]
print(result)