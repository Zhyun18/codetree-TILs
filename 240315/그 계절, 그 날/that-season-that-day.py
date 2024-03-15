y,m,d=tuple(map(int,input().split()))

# 윤년 판단 코드 
def is_year(n):
    if n%4==0 and n%100==0:
        return False
    if n%4==0 and n%100==0 and n%400==0:
        return True 
    if n%4==0:
        return True 

# 달 판단 코드 
def is_month(n):
    if 1<=n<=12:
        if 3<=n<=5:
            return 'Spring'
        elif 6<=n<=8:
            return 'Summer'
        elif 9<=n<=11:
            return 'Fall'
        else:
            return 'Winter'
    else:
        return False 

# 일 판단 코드
def is_date(y,m,d):
    if str(m) in ['1','3','5','7','8','10','12']:
        if 1<=d<=31:
            return True 
        else:
            return False 
    if str(m) in ['4','6','9','11']:
        if 1<=d<=30:
            return True 
        else: 
            return False 
    if m==2:
        if is_year(y):
            if d>29:
                return False 
            else:
                return True 
        else:
            if d>28:
                return False 
            else:
                return True

# 출력 코드 
if is_date(y,m,d) and is_month(m):
    print(is_month(m))
else:
    print(-1)