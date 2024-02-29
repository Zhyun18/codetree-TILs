a=input()
b=input()
arr=list(a)

cnt=0
flag=False
for i in range(len(arr)):
    arr=arr[-1:]+arr[0:len(arr)-1]
    cnt+=1
    if arr==list(b):
        flag=True
        break

if flag==True:
    print(cnt)
else:
    print(-1)