n=int(input())
cnt=0
while 1:
    n//=2
    #print(n)
    cnt+=1

    if n==1:
        break
print(cnt)