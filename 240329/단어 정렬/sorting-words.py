n=int(input())
words=[]
for _ in range(n):
    words.append(input())

for w in sorted(words):
    print(w)