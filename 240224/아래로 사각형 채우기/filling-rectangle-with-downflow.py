n=int(input())
arr=[[0 for _ in range(n)] for _ in range(n)]

num=0
for i in range(n):
    for j in range(n):
        arr[i][j]=num+1
        num+=n
    num=i+1


for row in arr:
    for elem in row:
        print(elem,end=' ')
    print()