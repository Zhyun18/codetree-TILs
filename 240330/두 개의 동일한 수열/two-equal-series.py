n=int(input())
a=list(input().split())
b=list(input().split())

flag=True
for elem in a: 
    if elem not in b:
        flag=False 

if flag==True:
    print('Yes')
else:
    print('No')