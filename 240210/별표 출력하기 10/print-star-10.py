n=int(input())
for i in range(1,n*2+1): # i = 1,2,3,4,5,6
    #print(i,end='')
    if i%2==0:
        for j in range(n-(i-1)//2):  
            print('*',end=' ')

    else:
        for k in range(i//2+1): # k = 1,2,3 ...
            print('*',end=' ')
    print()