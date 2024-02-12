start,end=map(int,input().split())
# 완전수 : 자기 자신을 제외한 모든 양의 약수를 더했을 때 자기 자신이 되는 수 
cnt=0
for i in range(start,end+1):
    sum_val=0 # 새로운 i 
    for j in range(1,i+1):
        if i%j==0 and j!=i:
            sum_val+=j
    if sum_val==i: # 최종값 비교 
        cnt+=1
print(cnt)