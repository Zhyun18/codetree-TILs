n=int(input())

# 감소전 별
for i in range(1,n+1): # i = 1,2,3,
    for j in range(1,i+1):
        #print(j,end='')
        print('*',end=' ')
    print()

# 걈소후 별
for i in range(n-1,0,-1):
    for j in range(i,0,-1):
        print('*',end=' ')
    print()