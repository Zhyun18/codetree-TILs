a,b=tuple(map(int,input().split()))
def solution(a,b):
    # 변수 설정 
    if a>b:
        a=a+25
        b=b*2
        return a,b
    else:
        b=b+25
        a=a*2
        return a,b 

for i in solution(a,b):
    print(i,end=' ')