n=int(input())
arr=[num for num in list(map(int,input().split()))]
def solution(arr):
    for elem in arr: 
        if elem<0:
            elem=elem * -1 
            print(elem,end=' ')
        else:
            print(elem,end=' ')

solution(arr)