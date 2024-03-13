m,d=tuple(map(int,input().split()))
def solution(m,d):
    month=[i for i in range(1,13)]
    date=[]
    if m==2:
        date=[str(i) for i in range(1,29)]
        if str(d) in date:
            return True
        else:
            return False 

    elif str(m) in ['1','3','5','7','8','10','12']:
        date=[str(i) for i in range(1,32)] 
        if str(d) in date:
            return True 
        else:
            return False 
    else:
        date=[str(i) for i in range(1,31)] 
        if str(d) in date:
            return True 
        else:
            return False 

if solution(m,d):
    print('Yes')
else:
    print('No')