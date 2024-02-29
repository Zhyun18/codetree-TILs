arr_2nd=[[0 for _ in range(5)] for _ in range(5)]
num=1
for i in range(5):
    for j in range(5):
        arr_2nd[i][0]=1
        arr_2nd[0][j]=1

for i in range(1,5):
    for j in range(1,5):
        arr_2nd[i][j]=arr_2nd[i-1][j]+arr_2nd[i][j-1]


for row in arr_2nd:
    for elem in row:
        print(elem,end=' ')
    print()