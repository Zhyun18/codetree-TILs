n=int(input())
cnt=1
for i in range(1,n+1):
    if i%2==1:
        for j in range(1,n+1):
            print(cnt,end=' ')
            cnt+=1
    else: 
        for j in range(n):
            print(cnt-1,end=' ')
            cnt-=1
    cnt+=n
    print()