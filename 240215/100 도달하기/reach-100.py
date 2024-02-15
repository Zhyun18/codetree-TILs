n=int(input())
arr=[1,n]
for i in range(2,101):
    arr.append(arr[i-2]+arr[i-1])
    if arr[i]>100:
        break

for i in arr:
    print(i,end=' ')