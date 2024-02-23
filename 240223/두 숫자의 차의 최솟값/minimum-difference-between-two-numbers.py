n=int(input())
arr=list(map(int,input().split())) # n개의 숫자가 오름차순 

# 서로 다른 두 개의 숫자를 골랐을 떄의 차이의 최솟값
ans=[]
for i in range(len(arr)):
    for j in range(1,len(arr)):
        if i!=j and arr[i]<arr[j]:
            ans.append(arr[j]-arr[i])
print(min(ans))