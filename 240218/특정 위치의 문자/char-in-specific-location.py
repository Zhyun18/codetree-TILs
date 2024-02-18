s=input()
arr=['L','E','B','R','O','S']

# 굳이 in/not 연산자 사용 반복문을 돌릴 필요가 없다~
if s not in arr:
    print('None')
else:
    print(arr.index(s))