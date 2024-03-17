# 함수 위의 값들을 정의하게 되면 어디에서 쓸 수 있는 global 변수가 됨 
string=input() # 입력 문자열 
def solution(s):
    # 주어진 입력 문자열에 대하여 목적 문자열이 부분 문자열로 존재하는 경우 
    # 부분 문자열의 시작 인덱스를 출력하는 코드를 작성 
    
    # 목적 문자열 
    o_string=input()
    if o_string in string:
        return string.index(o_string)
    else:
        return -1 

print(solution(string))