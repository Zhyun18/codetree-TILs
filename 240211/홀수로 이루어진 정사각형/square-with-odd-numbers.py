n=int(input())
for i in range(11,11+2*n,2): # i: 11,13
    for j in range(i,i+2*n,2):
        print(j,end=' ')
    print()