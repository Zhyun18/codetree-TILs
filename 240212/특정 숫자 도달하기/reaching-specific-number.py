_list=list(map(int,input().split()))
# 250 이상의 정수가 주어지면, 마지막으로 주어진 수를 제외하고 주어진 모든 정수들의 합계와 평균을 구하는 프로그램
sum_val=0
cnt=0
avg_val=0

for i in range(len(_list)):
    if _list[i]<250:
        sum_val+=_list[i]
        avg_val=sum_val/(i+1)
    if _list[i]>=250:
        break
print(f'{sum_val} {avg_val:.1f}')