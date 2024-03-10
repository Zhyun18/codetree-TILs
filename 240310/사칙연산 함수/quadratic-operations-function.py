a,b,c=tuple(input().split())
def solution(a,b,c):
    if b not in ['+','-','/','*']:
        return false
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