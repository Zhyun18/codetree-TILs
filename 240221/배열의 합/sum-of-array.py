arr_2nd=[list(map(int,input().split()))for _ in range(4)]
for i in arr_2nd:
    sum_val=0
    for j in i:
        sum_val+=j
    print(sum_val)