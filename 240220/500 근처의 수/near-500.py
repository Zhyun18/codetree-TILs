arr=list(map(int,input().split()))
ans1,ans2=[],[]
#0으로해야할까 배열안에 있는 숫자로 해야할까 고민중.. 
for i in arr:
    if i <500:
        ans1.append(i)
        max_num=max(ans1)
    elif i>=500:
        ans2.append(i)
        min_num=min(ans2)
print(max_num,min_num)