# 특정 코드의 아스키 코드 값 : ord()
a,b=map(ord,input().split())
if a>b:
    print(a+b,end=' ')
    print(a-b)
else:
    print(a+b,end=' ')
    print(b-a)