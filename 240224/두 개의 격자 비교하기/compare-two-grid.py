# 행의 개수, 열의 개수 입력
n,m=input().split()
n,m=int(n),int(m)

# n행 m열 격자 입력
arr1=[list(map(int,input().split()))for _ in range(n)]
arr2=[list(map(int,input().split()))for _ in range(n)]

# n행 m열의 빈 이중 리스트 
arr=[[0 for _ in range(m)] for _ in range(n)]
num=1
# 두 개의 격자 비교: 같으면 0, 다르면 1 
for i in range(n):
    for j in range(m):
        if arr1[i][j]!=arr2[i][j]:
            arr[i][j]=num

# 출력 
for r in arr:
    for e in r:
        print(e,end=' ')
    print()