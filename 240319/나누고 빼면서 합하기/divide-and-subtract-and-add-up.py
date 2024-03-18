n,m=tuple(map(int,input().split()))
def solution(n,m):
    arr=[int(num) for num in input().split()]
    while True:
        sum_value=0
        for num in arr:
            if m%2==0:
                sum_value+=arr[m-1]
                m//=2
                if m==1:
                    sum_value+=arr[0]
                    break
            elif m%2==1:
                sum_value+=arr[m-1]
                m-=1
                if m==1:
                    sum_value+=arr[0]
        return sum_value 

print(solution(n,m))