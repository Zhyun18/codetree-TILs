arr=list(map(int,input().split()))
max_value=arr[0]
for i in range(len(arr)):
    if max_value<arr[i]:
        max_value=arr[i]
print(max_value)