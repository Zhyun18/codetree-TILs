# 입력창
n=int(input())

# 초기화 변수
cnt=0 

while True:
    if n>=1000:
        print(cnt)
        break
        
    if n%2==0:
        n=n*3+1
        cnt+=1
    else:
        n=n*2+2
        cnt+=1