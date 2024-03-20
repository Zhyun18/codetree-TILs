n,m=tuple(map(int,input().split()))
def solution():
    global a
    a=list(map(int,input().split())) 
    for _ in range(m):
        sum_value=0
        a1,a2=tuple(map(int,input().split()))
        for num in a[a1-1:a2]:
            sum_value+=num 
        print(sum_value)

solution()