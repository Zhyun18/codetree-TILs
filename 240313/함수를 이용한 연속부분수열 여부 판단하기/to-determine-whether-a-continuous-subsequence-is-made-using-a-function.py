n1,n2=tuple(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))

# 수열 B가 수열 A의 연속부분 수열인지 판단
def solution(a,b):
    start=0
    end=0
    for i in range(len(a)):
        if b[0]==a[i:]:
            start=i
        if b[-1]==a[i]:
            end=i+1
    if a[start+1:end]==b:
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
#     if b[0]==a[i:]:
#         start=i
#     if b[-1]==a[i]:
#         end=i+1
# print(a[start+1:end])
# print(b)
# if a[start+1:end]==b:
#     print('응')
# else:
#     print('아니')