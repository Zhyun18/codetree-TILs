a,b=map(int,input().split())
ans=a+b
cnt=0
for elem in str(ans):
    if elem=='1':
        cnt+=1
print(cnt)