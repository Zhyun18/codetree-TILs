n=int(input())

for i in range(n):
    for k in range(i):
        print(' ',end=' ')
    for j in range(n-i,0,-1):
        print(j,end=' ')
    print()