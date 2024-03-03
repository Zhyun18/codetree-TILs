a=input()
b=input()
arr=list(a)

while True:
    idx=''.join(arr).index(b) # b 가 a 에 포함된 최초의 위치 
    arr=arr[:idx]+arr[idx+1:] # slicing 
    if b in ''.join(arr):
        arr=arr[:idx]+arr[idx+1:]
    else:
        arr=arr[:idx]+arr[idx+1:]
        break
print(''.join(arr))