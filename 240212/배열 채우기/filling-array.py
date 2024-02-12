arr=list(map(int,input().split()))
answer=[]
for i in range(len(arr)):
    if arr[i]==0:
        answer=arr[i-1::-1]
        for i in answer:
            print(i,end=' ')