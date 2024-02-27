str1=input()
str2=input()

ans1=''
ans2=''

for e in str1:
    if e.isdigit():
        ans1+=e

for e in str2:
    if e.isdigit():
        ans2+=e

print(int(ans1)+int(ans2))