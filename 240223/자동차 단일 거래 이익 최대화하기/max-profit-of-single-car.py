n=int(input()) # n년 
arr=list(map(int,input().split())) # 향후 n년간 자동차 가격 정보 

# 자동차를 단한번 사서 되팔때 최대이익 출력
# i 번째의 가격이 i+1,i+2,,,i+n-i 번째의 가격보다 작은 것들 중에 
result=[]
for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]< arr[j] and i < j:
            result.append(arr[j]-arr[i])

if len(result)==0:
    print(0)
else:
    print(max(result))