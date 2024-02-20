n=int(input())
arr=list(map(int,input().split()))

# 주어진 숫자들 중 최대값의 위치를 출력 -> 최대값이 여러 개라면 가장 왼쪽에 있는 최대값의 위치 출력
# 구한 최대값의 위치보다 더 왼쪽에 있는 숫자들 중 최대값을 구해 그 위치를 출력 
# 위 과정을 반복하여 최종적으로 첫 번째 원소가 뽑히게 되면 종료 (최종적으로 1값이 리턴되야함)

result=[]
while True:
    if 1 in result:
        break
    max_value=0
    idx=0
    for i in arr:
        if max_value<i:
            max_value=i
            idx=arr.index(max_value)
            result.append(idx+1)
    for i in arr[:idx+1]:
        if max_value<i:
            max_value=i
            idx=arr.index(max_value)
            result.append(idx+1)

max_index=0
for i in result[::-1]:
    print(i,end=' ')