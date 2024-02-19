# 수열 A : n1개의 원소로 이루어짐
# 수열 B : n2개의 원소로 이루어짐 
# 수열 B가 수열 A의 연속부분수열인지 판단하는 프로그램
# 수열 B가 수열 A의 원소들을 연속하게 뽑았을때 나올 수 있는 수열 -> 연속부분수열 

# 수열 a의 개수를 나타내는 n1, 수열B n2의 원소의 개수를 나타내는 값 공백 입력
a,b=map(int,input().split())

# 수열 A에 해당하는 n1개의 원소가 공백을 사이에 두고 주어짐
arr_a=[i for i in list(map(int,input().split()))]

# 수열 B
arr_b=[i for i in list(map(int,input().split()))]

# 연속부분함수임을 판단
# 끝에 있는 경우 
# flag=False 
# for i in range(len(arr_a)):
#     if arr_a[i:len(arr_a)]==arr_b:
#         flag=True

# 중간에 있는 경우 (슬라이싱을하자 min/max 이용)
idx=[]
for i in range(len(arr_a)):
    for j in range(len(arr_b)):
        if arr_a[i]==arr_b[j]:
            idx.append(i)

s,e=min(idx),max(idx)
for i in range(s,e+1):
    if arr_a[i:e+1]==arr_b:
        flag=True

if flag==True:
    print('Yes')
else:
    print('No')