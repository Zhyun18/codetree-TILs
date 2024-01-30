a=int(input())
if a%2==0:
    a=a//2
    if a%2!=0:
        print((a+1)//2)
    else:print(a)
else:
    print((a+1)//2)