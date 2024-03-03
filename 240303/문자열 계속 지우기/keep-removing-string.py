a=input()
b=input()
arr=list(a)


while True:
    if b in ''.join(arr):
        idx=''.join(arr).index(b)
        arr=arr[:idx]+arr[idx+len(b):]
        continue
    else:
        break
print(''.join(arr))