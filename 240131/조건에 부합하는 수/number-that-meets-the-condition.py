a=int(input())
# 다음의 조건을 모두 만족하지 않은 수 출력

for i in range(1,a+1):

    # 첫 번째 조건 
    if i%2==0 and i%4!=0:
        continue
    
    # 두 번째 조건 
    if (i//8)%2==0:
        continue 
    
    # 세 번째 조건
    if (i%7)<4:
        continue

    print(i,end=' ')