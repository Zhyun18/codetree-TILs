arr_2nd=[list(input().split()) for _ in range(5)]
for i in arr_2nd:
    for j in i:
        print(j.upper(),end=' ')
    print()