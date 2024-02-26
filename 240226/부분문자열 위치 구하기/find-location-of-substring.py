string=input()
obj=input()
temp=''
if obj==string:
    print(0)
elif obj in string:
    print(string.index(obj))
    
else:
    print(-1)