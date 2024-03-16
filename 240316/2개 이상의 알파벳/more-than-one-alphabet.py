a=input()
def solution(s):
    string=a[0]
    for i in range(1,len(a)):
        if a[i]!=string:
            return 'Yes'
        else:
            return 'No'

print(solution(a))