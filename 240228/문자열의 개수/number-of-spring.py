cnt=0
ans=[]
while True:
    s=input()
    cnt+=1
    if s=='0':
        break
    else:
       if cnt%2==1:
        ans.append(s)
    
print(cnt-1)    
for elem in ans:
    print(elem)