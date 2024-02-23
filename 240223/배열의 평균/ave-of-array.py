arr=[list(map(int, input().split())) for _ in range(2)]
# 가로평균
for i in arr:
    print(f'{sum(i)/len(i):.1f}',end=' ')
print()

# 세로평균
for i in range(4):
    sum_value=0
    for j in range(2):
        sum_value+=arr[j][i]
    print(f'{sum_value/2:.1f}',end=' ')
print()

# 전체 평균
sum_value=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum_value+=arr[i][j]
print(f'{sum_value/8:.1f}')