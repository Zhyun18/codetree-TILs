n=int(input())
def solution(n):
    if n%4!=0:
        return False 
    if n%100==0 and n%400!=0:
        return False 
    if n%4==0:
        return True

if solution(n)==True:
    print('true')
else:
    print('false')