n,m=tuple(map(int,input().split()))
def solution(n,m):
    ans=[]
    for i in range(1,100+1): # 100까지 포함해야지
        if n%i==0 and m%i==0:
            ans.append(i)
    print(max(ans))

solution(n,m)