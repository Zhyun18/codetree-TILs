s=input()
answer=''
for elem in s:
    if elem<='z' and elem>='a':
        answer+=elem.upper()
    if elem<="Z" and elem>='A':
        answer+=elem.lower()
print(answer)