n=int(input())
cnt=0
while 1:
    if 2**cnt==n:
        cnt+=1
        break
    else:
        n//=2
        cnt+=1
print(cnt)