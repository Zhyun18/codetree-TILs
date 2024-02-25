arr=['apple','banana','grape','blueberry','orange']
s=input()
cnt=0

for i in range(len(arr)):
    if arr[i][2]==s or arr[i][3]==s:
        print(arr[i])
        cnt+=1
print(cnt)