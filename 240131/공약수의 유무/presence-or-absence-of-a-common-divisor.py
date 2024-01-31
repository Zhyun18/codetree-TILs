# 입력창
a,b=input().split()
a,b=int(a),int(b)

# a이상 b이하의 수 중에서 1,920과 2,880의 공약수가 존재하는지 판단
for n in range(a,b+1):
    if (1920%n==0) and (2880%n==0):
        print(1)
        break
    else:
        print(0)
        break