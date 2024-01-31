a,b,c=input().split()
# 대소비교가 안된 이유 -> a,b,c 가 int 형이 아니었음
a,b,c=int(a),int(b),int(c)
arr=list(map(int,[a,b,c]))
if a==min(arr):
    print(1,end=' ')
else:
    print(0,end=' ')

if a==b and b==c and c==a:
    print(1)
else:
    print(0)