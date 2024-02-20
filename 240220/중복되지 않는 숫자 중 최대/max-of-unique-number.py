n=int(input())
arr=list(map(int,input().split()))
max_value=arr[0]
# 중복하지 않은 숫자 중. 최대값 출력, 존재하지 않는다면 -1 
for i in arr:
    if max_value<i:
        max_value=i

arr.remove(max_value)

flag=True
for i in arr:
    if max_value in arr:
        flag=False

if flag==True:
    print(max_value)
else:
    print(-1)