s=list(input())
while len(s)>1:
    num=int(input())
    if num>len(s)-1:
        num=-1
        s.pop(-1)
        print(''.join(s))
    else:
        s.pop(num)
        print(''.join(s))