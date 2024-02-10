n=int(input())
for i in range(1,n+1): # i: 1,2,3
    for j in range(n-i-1,-1,-1): # j: 2,1,0
        print('',end=' ')
    for k in range(i): # k : 1,2,3
        print('*',end=' ')
    print()

for i in range(n-1,0,-1): # i : 2,1   
    for j in range(1,n-i+1): # j: 1,2
        print('',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()