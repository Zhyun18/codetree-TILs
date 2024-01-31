n=int(input())

for i in range(n):
    # 한 줄에 입력받을 별의 수 
    for j in range(0,i+1):
        print('*',end='') 
    print()
    print()

for i in range(n,0,-1):
    # 한 줄에 입력받을 별의 수 
    for j in range(i-1,0,-1):
        print('*',end='') 
    print()
    print()