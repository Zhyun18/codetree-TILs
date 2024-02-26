string=input()
obj=input()
temp=''
for i in range(len(string)-1):
    temp=string[i]+string[i+1]
    if obj==temp:
        print(i)
        break
    elif obj==string:
        print(0)
        break
    else:
        print(-1)
        break