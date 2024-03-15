n=int(input())
arr=[num for num in list(map(int,input().split()))]
def solution(arr):
    return [num//2 if num%2==0 else num for num in arr]

for elem in solution(arr):
    print(elem,end=' ')