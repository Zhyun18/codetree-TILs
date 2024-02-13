n=int(input())
arr=list(map(int,input().split()))
# 짝수만 거꾸로 출력 -> 원 배열을 거꾸로 하면 됨 ㅋ 
for i in arr[::-1]:
    if i%2==0:
        print(i, end=' ')