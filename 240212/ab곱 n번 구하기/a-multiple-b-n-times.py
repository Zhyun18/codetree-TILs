n=int(input())
prod=1
for _ in range(n):
    a,b=map(int,input().split())
    for i in range(a,b+1):
        prod*=i
    print(prod)
    prod=1 # 초기화