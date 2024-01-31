# 첫 번째 입력창 
n=int(input())
i=0
# 두 번째 입력창 : 
for _ in range(n):
    i=int(input()) 
    if i%2==1 and i%3==0:
        print(i)