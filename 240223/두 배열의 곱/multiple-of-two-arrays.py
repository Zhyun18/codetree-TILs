arr_1=[list(map(int,input().split())) for _ in range(3)]
blank=input() # 입력에서 받은 공백을 받아야함 
arr_2=[list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        num=arr_1[i][j]*arr_2[i][j]
        print(num,end=' ')
    print()