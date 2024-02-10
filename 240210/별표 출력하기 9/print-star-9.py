n=int(input())

for i in range(1,n+1): # i: 1,2,3
    #공백 반복 j: 2,1,0
    for j in range(n-i,0,-1):
        print(' ',end=' ')
    
    # 별 반복 k : 1,3,5
    for k in range(2*i-1):
        print('*',end=' ')
    print()