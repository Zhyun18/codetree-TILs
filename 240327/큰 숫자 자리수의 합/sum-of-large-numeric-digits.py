arr=list(map(int,input().split()))
x,y,z=arr[0],arr[1],arr[2]
n=x*y*z
def solution(n):
    if n<10:
        return n
    return solution(n//10) + (n%10)
print(solution(n))