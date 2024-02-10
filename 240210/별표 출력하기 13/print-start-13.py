n=int(input())
for i in range(1,n*2+1):
    if i%2==1:
        for j in range(n-(i-1)//2,0,-1):
            print('*',end=' ')
    else:
        for k in range(i//2):
            print('*',end=' ')
    print()