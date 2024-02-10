n=int(input())
# 별 모양 규칙 : 2n-1, 1,3,5...
# 공백 규칙, 2,1,0...

for i in range(1,n+1): # i=1,2
    for j in range(n-i-1,-1,-1):
        print('',end=' ')
    for k in range(2*i-1):
        print('*',end='')
    print()

# 반대로
for i in range(n-1,0,-1): # i: 2,1
    for j in range(n-i): # j: 2.1
        print('',end=' ')
    for k in range(2*i-1): # k: 3,1 
        print('*',end='')
    print()