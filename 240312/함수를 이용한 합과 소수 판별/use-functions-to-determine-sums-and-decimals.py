a,b=tuple(map(int,input().split()))



def solution(n):
    for num in range(2,n):
        if n%num==0:
            return False
    if ((n//10)+(n%10))%2==0:
        return True 

cnt=0
for i in range(a,b+1):
    if solution(i):
        cnt+=1
print(cnt)