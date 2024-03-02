a=input()
b=input()
tmp=''
while True:
    idx=a.index(b)
    tmp=a[:idx]    
    if b in tmp:
        continue
    else:
        break
print(tmp)