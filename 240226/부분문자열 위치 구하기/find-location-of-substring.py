string=input()
obj=input()
temp=''
for i in range(len(string)-1):
    temp=string[i]+string[i+1]
    if obj==temp:
        print(i)
        break