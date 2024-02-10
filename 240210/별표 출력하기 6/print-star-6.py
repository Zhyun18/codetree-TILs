n=int(input())
# 별의 개수 규칙: 2n-1, 3 -> 1 
# 공백의 개수 규칙: 0, 1, 2 ,,, n-1 
# 첫 대칭
for i in range(n,0,-1):
    # 공백 반복 
    for j in range(0,n-i):
        print(' ',end=' ')
    # 별 반복 
    for k in range(2*i-1,0,-1):
        print('*',end=' ')
    print() 

# 두 번째 대칭
for i in range(1,n):
    for j in range(n-i,1,-1):
        print(' ',end=' ')
    for k in range(0,2*i+1):
        print('*', end=' ')
    print()