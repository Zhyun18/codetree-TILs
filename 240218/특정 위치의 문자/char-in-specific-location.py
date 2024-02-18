s=input()
arr=['L','E','B','R','O','S']
idx='None'
for i in arr:
    if s not in arr:
        print(idx)
        break
    else:
        print(arr.index(s))
        break