n=int(input())
arr=list(map(int,input().split()))

tmp1=list(sorted(arr))
for num in tmp1:
    print(num,end=' ')
print()

tmp2=list(sorted(arr,reverse=True))
for num in tmp2:
    print(num,end=' ')