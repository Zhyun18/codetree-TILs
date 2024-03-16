a,b=tuple(map(int,input().split()))
def solution(a,b):
    if a<b:
        a=a+10
        b=b*2
        return a,b
    else:
        a=a*2
        b=b+10
        return a,b

a,b=solution(a,b)
print(a,b)