string=input()
obj=input()
temp=''
for i in range(len(string)-1):
    if obj in string:
        print(string.index(obj))
        break
    else:
        print(-1)
        break