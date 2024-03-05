a,b,c=tuple(map(int,input().split()))
def solution(*args):
    ans=[]
    ans.append(args)
    return min(args)

print(solution(a,b,c))