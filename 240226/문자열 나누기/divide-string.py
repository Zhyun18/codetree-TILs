n=int(input())
strings=input().replace(' ','')
answer=''
for i in range(0,len(strings),5):
    answer+=strings[i:i+5]
    print(answer)
    answer=''