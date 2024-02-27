s=input()
answer=''
for elem in s:
    if elem.isalpha():
        answer+=elem 
    if elem.isdigit():
        answer+=elem
print(answer.lower())