arr=list(map(int,input().split()))
count_arr=[0]*101
for elem in arr: 
    result=(elem//10)*10
    if elem==0:
        break
    elif result>=10:
        count_arr[result]+=1
   
for i in range(100,9,-10):
    print(f'{i} - {count_arr[i]}')