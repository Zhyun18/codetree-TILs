# 각 진료소로 보내진 인원 출력, 긴급 상황일 경우 출력
a,b,c,d=0,0,0,0
e='E'
for i in range(3):
    arr=input().split()
    s,t=arr[0],int(arr[1])
    cnt=0
    if s=='Y' and t>=37:
        a+=1
    elif s=='N'and t>=37:
        b+=1
    elif s=='Y'and t<37:
        c+=1
    else:
        result='D'
        d+=1

if a>=2:
    print(a,b,c,d,e, sep=' ')
else:
    print(a,b,c,d, sep=' ')