a,n=input().split()
a,n=int(a),int(n)
for i in range(n+1):
    a+=n
    print(a)
    i+=1
    if i==n:
        break