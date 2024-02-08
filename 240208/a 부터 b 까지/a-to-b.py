a,b=map(int,input().split())
num=a

for i in range(a,b+1):
    i=num
    print(num,end=' ')
    if num%2==1:
        num=i*2
    else:
        num=i+3
    if num>b:
        break