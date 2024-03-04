n,m=tuple(map(int,input().split()))
def solution(n,m):
    ans=[]
    for i in range(1,101):
        if i%n==0 and i%m==0:
            ans.append(i)
    print(min(ans))
solution(n,m)