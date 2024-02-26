strings=list(input())
for i in range(len(strings)):
    if i==1 or i==len(strings)-2:
        strings[i]=''
print(''.join(strings))