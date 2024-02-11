n=int(input())
cnt=n
for i in range(1,n+1):
    for j in range(i):
        print(cnt+j,end=' ')
    cnt-=1
    print()