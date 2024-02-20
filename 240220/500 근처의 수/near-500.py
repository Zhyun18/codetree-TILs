arr=list(map(int,input().split()))
#0으로해야할까 배열안에 있는 숫자로 해야할까 고민중.. 
ans=[]
for i in range(len(arr)):
    if arr[i]<500:
        max_num=arr[i]
        if max_num<arr[i]:
            max_num=arr[i] 
    else:
        ans.append(arr[i])    
        min_num=min(ans)
print(max_num,min_num)