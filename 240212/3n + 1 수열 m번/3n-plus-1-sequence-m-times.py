n=int(input())
# n에서 시작해서 n이 짝수면 2로 나누고, n이 홀수면 3을 곱하고 1을 더해서 n이 1이 되기 전ㄲ싸지 계속 반복
cnt=0
for _ in range(n):
    num=int(input())
    while True:
        if num==1:
            break
        elif num%2==0:
            num//=2
            cnt+=1
        elif num%2==1:
            num=num*3+1
            cnt+=1
print(cnt)