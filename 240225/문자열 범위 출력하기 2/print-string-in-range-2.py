s=input()
n=int(input())
arr=[]
for elem in s[-n:]:
    arr.append(elem)
print(''.join(arr[::-1]))