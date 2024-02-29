cnt=0
for _ in range(3):
    sym,temp=input().split()
    temp=int(temp)
    if sym=='Y' and int(temp)>=37:
        cnt+=1

if cnt>=2:
    print('E')
else:
    print('N')