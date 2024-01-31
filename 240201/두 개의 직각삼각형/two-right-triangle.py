n=int(input())
# n행 생성 
for i in range(n,-1,-1):
    # 한 행에 반복할 별 작성 
    for j in range(i,0,-1):
        print('*',end='')

    # 한 행에 반복할 공백 작성
    for j in range(n-i):
        print('  ',end='') 
   
    for j in range(i,0,-1):
        print('*',end='')
    print()