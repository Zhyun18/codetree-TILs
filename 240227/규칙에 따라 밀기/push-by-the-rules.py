s=input()
arr=list(s)
c=input()

# 'L'커맨드 : arr=arr[1:]+arr[0:1]
# 'R'커맨드 : arr=arr[len(arr)-1:len(arr)]+arr[0:len(arr)-1]

for i in range(len(c)):
    if c[i]=='L':
        arr=arr[1:]+arr[0:1]
    
    else:
        arr=arr[len(arr)-1:len(arr)]+arr[0:len(arr)-1]
        
print(''.join(arr))