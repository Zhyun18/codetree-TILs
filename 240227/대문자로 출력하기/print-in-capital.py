s=input()
answer=''
for elem in s:
    if elem.isalpha():
        answer+=elem 
print(answer.upper())