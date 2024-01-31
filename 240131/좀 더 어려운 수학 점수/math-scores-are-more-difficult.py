a1,a2=input().split() # 수학,영어 순서
a1,a2=int(a1),int(a2)

b1,b2=input().split()
b1,b2=int(b1),int(b2)

# 수학점수가 높은 학생의 이름 출력
if a1>b1:
    print('A')
elif a1<b1:
    print('B')
else:
    if b1>b2:
        print('A')
    elif b1<b2:
        print('B')