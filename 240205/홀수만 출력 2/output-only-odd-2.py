b,a=input().split()
b,a=int(b),int(a)

if b%2==1:
    for i in range(b,a-1,-2):
        print(i, end=' ')
else:
    for i in range(b-1,a-1,-2):
        print(i, end=' ')