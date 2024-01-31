# 입력창
n = int(input())
cnt=0
# n 을 차례대로 1부터 나누었을 때 1 이하가 되는 순간 까지 나눗셈을 진행한 횟수 
for i in range(1,n+1):
    n//=i
    cnt+=1
    if n<=1:
        break
print(cnt)