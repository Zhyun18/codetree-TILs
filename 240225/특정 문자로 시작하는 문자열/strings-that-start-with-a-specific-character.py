n=int(input())
arr=[]
for _ in range(n+1):
    s=input()
    arr.append(s)

cnt=0
sum_value=0
for i in range(len(arr)-1):
    if arr[-1]==arr[i][0]:
        cnt+=1
        sum_value+=len(arr[i])
print(f'{cnt} {sum_value/cnt:.2f}')