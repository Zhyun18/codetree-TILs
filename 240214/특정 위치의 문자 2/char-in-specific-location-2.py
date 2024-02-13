arr=list(input().split())
for i in range(len(arr)):
    if i==2 or i==5 or i==8:
        print(arr[i-1],end=' ')