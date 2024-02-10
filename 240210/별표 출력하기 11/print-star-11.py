n=int(input())
# 공백 : (0부터 시작 기준) : 1,3,5
for i in range(2*n+1):
    for j in range(2*n+1):
        if (i%2==1 and j%2==1):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()