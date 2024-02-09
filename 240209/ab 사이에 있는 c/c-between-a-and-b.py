a,b,c=map(int,input().split())
flag=False
for i in range(a,b+1):
    if i%c==0:
        flag=True

if flag==True:
    print('YES')
else:
    print('NO')