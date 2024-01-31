# 입력창
a,b=input().split()
a,b=int(a),int(b)

result=0 

# a 이상 b 이하의 수 
for i in range(a,b+1):
    if i%6==0 and i%8!=0:
        result+=i
print(result)