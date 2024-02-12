n=int(input())
cnt=65
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print(chr(cnt),end=' ')
        cnt+=1
        if cnt>90: # 아스키코드 90이후 다시 65부터 (주의)
            cnt=65
    print()