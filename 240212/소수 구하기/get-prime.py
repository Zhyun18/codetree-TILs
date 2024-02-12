n=int(input())
for i in range(2,n+1):
    flag=True
    for j in range(2,i):
        if i%j==0 and j!=i:# 소수 : 1과 자신이외의 약수를 안 갖는 수
            flag=False
    if flag==True:
        print(i,end=' ')