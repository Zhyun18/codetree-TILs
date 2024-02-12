n=int(input())
x='A'
cnt=ord(x)
for i in range(n):
    for j in range(n):
        print(chr(cnt),end='')
        cnt+=1
    print()