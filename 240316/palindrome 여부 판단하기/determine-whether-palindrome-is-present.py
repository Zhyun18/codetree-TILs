a=input()
def solution(s):
    if s==s[::-1]:
        return 'Yes'
    else:
        return 'No'
            
print(solution(a))