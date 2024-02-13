arr=list(map(int,input().split()))
ans=[]
flag=False
for i in range(len(arr)):
    if arr[i]==0:
        flag=True
    
if flag==False:
    ans=arr[i::-1]
    for j in ans:
        print(j,end=' ')
else:
    ans=arr[i-1::-1]
    for j in ans:
        print(j, end=' ')