n=int(input())
arr_2nd=[[0 for _ in range(n)] for _ in range(n)]
num=1

for i in range(n): 
    for j in range(n):
        arr_2nd[i][0]=1
        arr_2nd[0][j]=1

for i in range(1,n):
    for j in range(1,n):
        arr_2nd[i][j]=arr_2nd[i-1][j]+arr_2nd[i-1][j-1]+arr_2nd[i][j-1]

for row in arr_2nd:
    for elem in row:
        print(elem,end=' ')
    print()