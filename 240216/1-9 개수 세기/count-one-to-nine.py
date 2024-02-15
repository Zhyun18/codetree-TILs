n=int(input())
count_arr=[0 for _ in range(9)]
arr=list(map(int,input().split()))
for elem in arr:
    count_arr[elem-1]+=1
for i in count_arr:
    print(i)