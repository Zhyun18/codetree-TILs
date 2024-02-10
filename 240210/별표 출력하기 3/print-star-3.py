n=int(input())
 
for i in range(n):
    # 공백
    for j in range(i):
        print(' ',end=' ')

    # 별
    for j in range((n-i)*2-1,0,-1):
        print('*',end=' ')
    print()