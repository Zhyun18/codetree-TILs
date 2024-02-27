n=int(input())
sum_value=0
for _ in range(n):
    ans=input()
    sum_value+=int(ans)

print(str(sum_value)[1:]+str(sum_value)[0])