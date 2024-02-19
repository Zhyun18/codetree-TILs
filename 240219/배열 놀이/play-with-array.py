# 원소의 개수를 나타내는 n과 질의의 수를 나타내는 q 값이 공백을 사이에 두고 주어짐
n,q=map(int,input().split())

# n개의 원소가 공백을 사이에 두고 주어짐
arr=[int(i) for i in input().split()]

# q개의 줄에 걸쳐 질의가 주어짐. 각 질의는 3개 중 하나의 타입 
for _ in range(n):
    idx=[]
    _list=list(map(int,input().split()))
    if len(_list)==2:
        m,a=_list[0],_list[1]
        if m==1:
            print(arr[a-1])
        else:
            if a in arr:
                idx.append(arr.index(a))
                print(min(idx)+1)
    else:
        m,a,b=_list[0],_list[1],_list[2]
        for i in arr[a-1:b]:
            print(i,end=' ')