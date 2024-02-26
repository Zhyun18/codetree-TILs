s1='ee'
s2='eb'

string=input()

cnt=0
cnt2=0
temp=''

for i in range(len(string)-1):
    temp=string[i]+string[i+1]
    if temp=='ee':
        cnt+=1
    if temp=='eb':
        cnt2+=1

print(cnt,cnt2,sep=' ')