a,b,c=tuple(input().split())
def solution(a,b,c):
    if b not in ['+','-','/','*']:
        return False  # false 는 대문자로 쓰세요;; 
    else:
        if b=='+':
            return int(a)+int(c)
        if b=='-':
            return int(a)-int(c)
        if b=='/':
            return int(a)//int(c)
        if b=='*':
            return int(a)*int(c)
        
print(f'{a} {b} {c} = {solution(a,b,c)}')