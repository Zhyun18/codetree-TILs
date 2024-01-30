a=int(input())
if a%2==0:
    a=a//2
    if a%2!=0:
        print((a+1)//2)
elif a%2!=0:
    a+=1
    if a%2==0:
        print(a//2)