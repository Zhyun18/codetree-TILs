a,b=map(int,input().split())
arr=[a,b]
for i in range(2,10):
    arr.append((arr[i-2]*2)+arr[i-1])
for i in arr:
    print(i,end=' ')