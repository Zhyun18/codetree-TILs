# 원소의 개수 n 
n=int(input())

# n개의 정수
arr=[i for i in list(map(int,input().split()))]

# 내림차순 정렬 
ans=[]
max_value=arr[0]
second_value=arr[0]
for i in arr: 
    if max_value<i:
        max_value=i
    elif second_value<i:
        second_value=i

print(max_value,second_value)