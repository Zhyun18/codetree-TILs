n=int(input())
cnt=65
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print(chr(cnt),end=' ')
        cnt+=1
    print()