arr=[list(map(int, input().split())) for _ in range(2)]
# 가로평균
for i in arr:
    print(sum(i)/len(i),end=' ')
print()

# 세로평균
for i in range(4):
    sum_value=0
    for j in range(2):
        sum_value+=arr[j][i]
    print(sum_value/2,end=' ')
print()

# 전체 평균
sum_value=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum_value+=arr[i][j]
print(sum_value/8)