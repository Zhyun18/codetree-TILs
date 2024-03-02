a=input()
b=input()
tmp=''
while True:
    idx=a.index(b)
    tmp=a[:idx]    
    if b not in tmp:
        break
print(tmp)