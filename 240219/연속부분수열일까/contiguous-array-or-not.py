# 수열 a의 개수를 나타내는 n1, 수열B n2의 원소의 개수를 나타내는 값 공백 입력
a,b=map(int,input().split())

# 수열 A에 해당하는 n1개의 원소가 공백을 사이에 두고 주어짐
arr_a=[i for i in list(map(int,input().split()))]

# 수열 B
arr_b=[i for i in list(map(int,input().split()))]

# 연속부분함수임을 판단
# 끝에 있는 경우 
flag=False 
for i in range(len(arr_a)):
    if arr_a[i:len(arr_a)]==arr_b:
        flag=True

# 중간에 있는 경우 (슬라이싱을하자 min/max 이용)
idx=[]
idx2=[]
for i in range(len(arr_a)):
    for j in range(len(arr_b)):
        if arr_a[i]==arr_b[j]:
            idx.append(i)


if len(idx)==0:
    flag=False
else:
    for i in range(len(idx)-1):
        if idx[i]+1==idx[i+1]:
            idx2.append(idx[i])
    if len(idx2)==0:
        flag=False 
    else:
        s,e=min(idx2),max(idx2)
        if arr_a[s:e+2] == arr_b:
            flag=True

if flag==True:
    print('Yes')
else:
    print('No')