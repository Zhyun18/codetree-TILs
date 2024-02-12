arr=list(map(int,input().split()))
answer=[]
flag=True
for i in range(len(arr)):
    if arr[i]==0:
        answer=arr[i-1::-1]
        for i in answer:
            print(i,end=' ')
        flag=False
    if flag==True:
        print(arr[9-i],end=' ')