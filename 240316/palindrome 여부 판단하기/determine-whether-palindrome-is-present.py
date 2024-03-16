a=input()
def solution(s):
    if a.islower(): # 소문자 판단 메서드 : islower()
        return "Yes"
    else:
        return "No"

print(solution(a))