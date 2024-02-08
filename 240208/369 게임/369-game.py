n=input()
for i in range(1,int(n)+1):
    if str(i) in ['3','6','9']:
        print('0',end=' ')
    else:
        print(i,end=' ')