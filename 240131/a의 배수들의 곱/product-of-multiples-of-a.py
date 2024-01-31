# 입력창
a,b=input().split()
a,b=int(a),int(b) # 정수형 변환을 잊지말자! 
result=1 # 곱셈의 값을 받아야 하므로 초기화 변수는 0 이 아닌 1

# 1부터 b까지의 수 중 ~
for i in range(1,b+1):
    if i%a==0:
        result*=i
print(result)