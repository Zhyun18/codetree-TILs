# 입력창(격자크기) 
n=int(input())

# 빈 2차원 배열 (nxn) 생성
arr=[[0 for _ in range(n)] for _ in range(n)]
num=1

# 격자 규칙 구현
for c in range(n-1,-1,-1): # n=4, i: 3,2,1,0
    if c%2!=0:
        # Case1 
        for r in range(n-1,-1,-1):
            arr[r][c]=num 
            num+=1 
    else: 
        # Case 2 
        for r in range(n):
            arr[r][c]=num 
            num+=1        


# 격자 출력
for r in arr:
    for e in r:
        print(e,end=' ')
    print()