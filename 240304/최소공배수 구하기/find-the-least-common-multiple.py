n,m=tuple(map(int,input().split()))
def solution(n,m):
    ans=0
    for i in range(1,101):
        if i%n==0 and i%m==0:
            ans=i
            break
    print(ans)
solution(n,m)