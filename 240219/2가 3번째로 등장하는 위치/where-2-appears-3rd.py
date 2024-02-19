n=int(input())
arr=[i for i in list(map(int,input().split()))]
cnt=0
answer=0
for i in arr:
    if i==2:
        cnt+=1
    if cnt==3:
        answer=arr.index(i)-1
print(answer)