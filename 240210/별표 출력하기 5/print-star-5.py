n=int(input())
for i in range(n,0,-1): # i : 4,3,2,1
    for j in range(1,i**2+1):
        print('*',end='')
        if j%i==0:
           print('',end=' ')
    print()