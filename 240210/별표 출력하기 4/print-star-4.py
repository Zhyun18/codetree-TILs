n=int(input())
# 대칭 전반부
for i in range(n): 
    for j in range(n-i,0,-1):
        print('*',end=' ')
    print()

# 대칭 후반부
for i in range(2,n+1):
    for j in range(i):
        print('*',end=' ')
    print()