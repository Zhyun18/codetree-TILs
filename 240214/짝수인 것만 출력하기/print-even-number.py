n=int(input())
arr=[i for i in list(map(int,input().split())) if i%2==0 ]
for i in arr:
    print(i,end=' ')