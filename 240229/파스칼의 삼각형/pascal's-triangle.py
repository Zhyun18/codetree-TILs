# 행의 크기 정수 n 
n=int(input())
arr=[ [ 0  for _ in range(n)] for _ in range(n)]

num=1
for i in range(n):
    for j in range(i+1):
        arr[i][j]=num
    
for i in range(2,n):
    for j in range(1,n-1):
        arr[i][j]=arr[i-1][j]+arr[i-1][j-1]        

for i in range(n):
    for j in range(n):
        if arr[i][j]==0:
            arr[i][j]=' '


for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()