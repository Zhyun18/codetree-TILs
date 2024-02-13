arr=list(map(int,input().split()))
# 0이 입력되면 10개 입력이 끝나지 않더라도 그때까지 입력한 합과 평균을 출력하는 프로그램 작성
# 0이 입력된 경우 0을 제외한 합과 평균을 구함 
sum_val=0
avg_val=0
cnt=0 # 0이 나오는 index

for i in arr:
    if i==0:
        break
    cnt+=1

for i in range(cnt):
    sum_val+=arr[i]
    avg_val=sum_val/(cnt)
print(f'{sum_val} {avg_val:.1f}')