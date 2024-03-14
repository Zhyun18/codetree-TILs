n1,n2=tuple(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# 수열 B가 수열 A의 연속부분 수열인지 판단
def solution(a,b):
    start=0
    end=0
    for i in range(len(a)):
        if b[0]==b[1]:
            b=b[1:]
        if b[0]==a[i]:
            start=i
        if b[-1]==a[i]:
            end=i
            break 
    if a[start:end+1]==b:
        return True  
    else:
        return False
        

if solution(a,b):
    print('Yes')
else:
    print('No')

# start=0
# end=0
# for i in range(len(a)):
#     if b[0]==b[1]:
#         b=b[1:]
#     if b[0]==a[i]:
#         start=i
#     if b[-1]==a[i]:
#         end=i
#         break 
# print(a[start:end])
# print(b)