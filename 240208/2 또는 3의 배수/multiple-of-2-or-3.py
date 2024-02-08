n=int(input())
# 2의 배수나 3의 배수 1, 아니면 0 
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        print(1, end=' ')
    else:
        print(0, end=' ')