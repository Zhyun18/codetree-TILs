arr=[]
for _ in range(11):
    s=input()
    arr.append(s)

flag=False
for i in range(len(arr)-1):
    if arr[i][-1]==arr[-1]:
        print(arr[i])
        flag=True

if flag==False:
    print('None')