a=input()
b=input()
arr=list(a)
tmp=''

while True:
    if b not in arr:
        break
    else:
        idx=arr.index(b)
        arr=arr[:idx]+arr[idx+1:]
print(tmp)