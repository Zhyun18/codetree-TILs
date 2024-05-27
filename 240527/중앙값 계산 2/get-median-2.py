n=int(input())
# 홀수 번째 수를 읽을 때 마다 지금까지 입력 받은 값 중앙 값을 차례대로 공백을 두고 출력  
answer=[]
arr=list(map(int,input().split()))
for i in range(n+1):
    if i%2==1:
        answer=sorted(arr[:i])
        print(answer[i//2],end=' ')