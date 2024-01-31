b,a=input().split() # b 와  a 가 주어짐
b,a=int(b),int(a)
my_list=[]
for i in range(a,b+1,2):
    my_list.append(i)
    answer_list=sorted(my_list,reverse=True)
for a in answer_list:
    print(a,end=' ')