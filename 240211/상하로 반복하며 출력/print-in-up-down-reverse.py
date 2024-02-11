n=int(input())
c1=1
c2=n
for i in range(n):
    for j in range(n):
        if j%2==0:
            print(c1,end='')
        else:
            print(c2,end='')
    c1+=1
    c2-=1
    print()