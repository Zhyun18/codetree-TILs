# 플래그 변수 선언 
flag=True 

# 모든 수가 3의 배수 or not? 
for _ in range(5):
    n=int(input())
    if n%3 != 0:
        flag=False

if flag==True:
    print(1)
else:
    print(0)