n=int(input())
arr=[i for i in list(map(int,input().split()))]
cnt=0
answer=0
for i in range(len(arr)):
    if arr[i]==2:
        cnt+=1
    if cnt==3:
        answer=i
        break
print(answer+1)