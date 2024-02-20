# 원소의 개수 n 
n=int(input())

# n개의 정수
arr=[i for i in list(map(int,input().split()))]

# 내림차순 정렬 
max_value=arr[0]
for i in arr: 
    if max_value<i:
        max_value=i

# 최대값 배열에서 삭제
arr.remove(max_value)
second_value=arr[0]
for i in arr:
    if second_value<i:
        second_value=i

print(max_value,second_value)