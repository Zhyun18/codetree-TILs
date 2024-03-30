str1=input()
str2=input()

def solution(str1,str2):
    if len(str1)!=len(str2):
        return False 
    else:    
        for elem in str1:
            if elem not in str2:
                return False 
        
        for elems in str2:
            if elems not in str1:
                return False 
    return True
    
if solution(str1,str2):
    print('Yes')
else:
    print('No')