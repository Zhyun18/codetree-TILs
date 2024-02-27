a,b=input().split()
answer=''
for elem in a:
    if not elem.isdigit():
        break
    else:
        answer+=elem
answer2=''
for elem in b:
    if not elem.isdigit():
        break
    else:
        answer2+=elem

print(int(answer)+int(answer2))