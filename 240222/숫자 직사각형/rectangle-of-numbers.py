n,m=map(int,input().split())
arr_2nd=[[0 for _ in range(m)] for _ in range(n)]
num=1
for i in range(n):
    for j in range(m):
        arr_2nd[i][j]=num 
        num+=1

for row in arr_2nd:
    for elem in row:
        print(elem,end=' ')
    print()