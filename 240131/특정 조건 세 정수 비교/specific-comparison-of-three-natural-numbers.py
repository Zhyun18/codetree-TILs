a,b,c=input().split()
arr=list(map(int,[a,b,c]))
if a==min(arr):
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b and b==c and c==a:
    pritn(1)
else:
    print(0)