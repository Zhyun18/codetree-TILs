n=int(input())
arr=[ i*n for i in range(1,11) ]
ans=[i for i in arr if i%5==0]
for i in range(10):
    print(arr[i],end=' ')
    if arr[i]==ans[1]:
        break