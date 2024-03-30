n=int(input())

# 배열의 개념으로 가야할지 말지 
# 배열을 함수 밖에서 선언해야할지 말지
arr=list(map(int,input().split()))

result=1
for elem in arr:
    if elem==1:
        result*=1

    elif elem%3==0:
        result*=3

    elif elem%5==0:
        result*=5

    elif elem%2==0:
        result*=2
    else:
        result*=elem 

print(result)