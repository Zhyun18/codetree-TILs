s=list(input())
for i in range(len(s)):
    if s[i]=='e':
        s[i]=''
        break
print(''.join(s))