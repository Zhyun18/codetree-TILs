# 소수 : 1과 자신만을 약수로 갖는 수 
n=int(input())
flag=True

for i in range(2,n):
    if n%i==0:
        flag=False

if flag==True:
    print('P')
else:
    print('C')