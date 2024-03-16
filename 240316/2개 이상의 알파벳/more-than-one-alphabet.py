a=input()
def solution(s):
    string=a[0]
    cnt=0
    for i in range(1,len(a)):
        if a[i]!=string:
            cnt+=1
    if cnt>=1:
        return "Yes"
    else:
        return "No"
print(solution(a))