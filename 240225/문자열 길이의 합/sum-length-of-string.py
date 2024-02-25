n=int(input())
arr=[]
sum_value=0
for _ in range(n):
    s=input()
    arr.append(s)

cnt=0
for i in range(len(arr)):
    sum_value+=len(arr[i])
    if 'a' in arr[i][0]:
        cnt+=1 
print(sum_value,cnt,sep=' ')