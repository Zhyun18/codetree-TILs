arr=list(map(int,input().split()))
ans=[]
flag=False
for i in range(len(arr)):
    if arr[i]==0:
        ans=arr[:i]
        flag=True
if flag==True:
    for j in ans[::-1]:
        print(j,end=' ')
else:
    for k in arr[::-1]:
        print(k,end=' ')