s,q=input().split()
arr=list(s)
q=int(q)

# 1:가장 앞 문자 제외 나마지 문자 한칸 앞 -> 가장 앞문자 가장 뒤
# 2: 가장 뒤 문자 제외 나머지 문자 한칸 뒤 -> 가장 뒷문자 가장 앞
# 3: 문자열 좌우 뒤집기 


# 갱신이 된 값으로 규칙을 적용해야 하는데 문자열은 immutable함 귀찮음! 
for _ in range(q):
    num=int(input())
    if num==1:
        arr=arr[1:]+arr[0:1]
        print(''.join(arr))

    if num==2:
        arr=arr[-1:]+arr[:-1]
        print(''.join(arr))

    # 반대 출력
    if num==3:           
        arr=arr[::-1]
        print(''.join(arr))