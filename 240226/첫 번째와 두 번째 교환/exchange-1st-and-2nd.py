s=input()
s_list=list(s)
one,two=s[0],s[1]
for i in range(len(s_list)):
    if s_list[i]==one:
        s_list[i]=two
    elif s_list[i]==two:
        s_list[i]=one 
print(''.join(s_list))