s1,s2=input().split()
if len(s1)>len(s2):
    print(s1,len(s1),sep=' ')
elif len(s2)>len(s1):
    print(s2,len(s2),sep=' ')
else:
    print('same')