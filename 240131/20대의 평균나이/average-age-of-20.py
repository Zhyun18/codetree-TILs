# 초기화 변수
result=0
cnt=0 

# 처음으로 20대가 아닌 다른 나이대의 사람이 나오기 전까지의 입력된 나이들의 평균
while True:
    # 입력창
    n=int(input())
    
    # 20대가 아니면 
    if not(20<=n<=29):
        print(f'{result/cnt:.2f}')
        break

    result+=n
    #print(result,end=' ')
    cnt+=1
    #print(cnt)