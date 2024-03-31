str1=input()
str2=input()

def solution(str1,str2):
    if sorted(str1)==sorted(str2):
        return True 
    else:
        return False 

if solution(str1,str2):
    print('Yes')
else:
    print('No')