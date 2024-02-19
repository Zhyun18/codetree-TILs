arr=list(map(int,input().split()))
max_value,min_value=arr[0],arr[0]
for i in arr:
    if i==999 or i==-999:
        break
    elif max_value<i and max_value!=999:
        max_value=i 
    elif min_value>i and min_value!=-999:
        min_value=i 
print(max_value, min_value)