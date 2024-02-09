# 완전수: 자기 자신을 제외한 약수의 합이 자신이 되는 수 
n=int(input())
sum_value=0
for i in range(1,n):
    if n%i==0:
        sum_value+=i

if sum_value==n:
    print('P')
else:
    print('N')