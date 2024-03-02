s,q=input().split()
arr=list(s)
tmp=''
q=int(q)

for _ in range(q):
    ques=input().split()
    if ques[0]=='1':
        q1,q2=int(ques[1]),int(ques[2])
        arr[q1-1],arr[q2-1]=arr[q2-1],arr[q1-1]
        print(''.join(arr))
    elif ques[0] =='2':
        q1,q2=ques[1],ques[2]
        print(''.join(arr).replace(q1,q2))