a1,g1=input().split()
a1=int(a1)

a2,g2=input().split()
a2=int(a2)

# 두 사람 중 한 사람이라도 19세 이상이면서 남자면 1 
# 여집합 개념 사용 -> 둘다 19세 미만, 여자인 경우가 0 나머지는 1

if (a1<19 and 'W' ==  g1 ) or (a2 <19and 'W' == g2):
    print(0)
else:
    print(1)