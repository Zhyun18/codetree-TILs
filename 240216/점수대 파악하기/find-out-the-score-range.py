arr=list(map(int,input().split()))
count_arr=[0]*101
for elem in arr: 
    count_arr[(elem//10)*10]+=1
for i in range(100,9,-10):
    print(f'{i} - {count_arr[i]}')