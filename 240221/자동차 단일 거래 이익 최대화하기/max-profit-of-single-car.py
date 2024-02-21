n=int(input()) # n년 
arr=list(map(int,input().split())) # 향후 n년간 자동차 가격 정보 

# 자동차를 단한번 사서 되팔때 최대이익 출력
# 입찰가 (가격 초기화가 제일 어려운 부분인 것 같다) 

min_value=arr[0]
idx=0
for i in range(len(arr)):
    if min_value>arr[i]:
        min_value=arr[i] 
        idx=i

max_value=arr[idx]

for i in range(idx,len(arr)):
    if max_value<arr[i]:
        max_value=arr[i]

print(max_value-min_value)