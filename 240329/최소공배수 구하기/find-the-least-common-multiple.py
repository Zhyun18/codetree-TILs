n,m=input().split()
n,m=int(n),int(m)
num=0
for i in range(2,n):
    if n%i==0 and m%i==0 and i*n%m==0: # 최대공약수
        num=i
        print(num*n) 
        break