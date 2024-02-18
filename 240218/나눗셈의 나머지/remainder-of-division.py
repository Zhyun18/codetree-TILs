# 두 정수a,b가 주어지면 a를 b로 나눈 몫을 a에 계속해서 저장 반복
# a가 1 이하가 되기 전까지 나눗셈 반복 
# 각 나눗셈 연산마다 나온 나머지들이 등장한 횟수를 제곱하여 그 합을 출력

a,b=map(int,input().split())

arr=[]
while True:
    if a<=1:
        break
    arr.append(a%b)
    a//=b

# 나온 횟수 세기 V
count_arr=[0]*(max(arr)+1) # 3 -> [0,0,0] 

for i in arr:
    count_arr[i]+=1

result=0
for i in count_arr: 
    result+=i**2
print(result)