n=int(input())
arr=list(map(int,input().split()))


# 중복하지 않은 숫자 중. 최대값 출력, 존재하지 않는다면 -1 
# 중복을 어떻게 세면 될까? 
ans=[]
for i in arr:
    if arr.count(i)==1:
        ans.append(i)

if len(ans)==0:
    print(-1)
else:
    max_value=ans[0]
    for i in ans:
        if max_value<i:
            max_value=i 
    print(max_value)