s=input()
one,two=s[0],s[1]
result=''
for i in list(s):
    if i==one:
        i=two 
    if i==two:
        i=one 
    result+=i
print(result)