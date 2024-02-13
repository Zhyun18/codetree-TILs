arr=list(map(int,input().split()))
ans=[]
for i in range(len(arr)):
    if arr[i]==0:
        ans=arr[:i]
    else:
        ans=arr[::]
for j in ans[::-1]:
    print(j,end=' ')