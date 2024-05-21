# 입력 
n,k,t=tuple(input().split())
n,k=int(n),int(k)

# t로 시작하는 단어 중에 사전순으로 정렬했을 때 k 번째 문자열 출력 
# 빈 리스트 
my_list=[]
for _ in range(n):
    s=input()
    if t in s: 
        my_list.append(s) 
print(sorted(my_list)[k-1])