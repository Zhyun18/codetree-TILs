a,b,c=map(int,input().split())
flag=True
for i in range(a,b+1):
    if i%c==0:
        flag=False

if flag==False:
    print('NO')
else:
    print('YES')