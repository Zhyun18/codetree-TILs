cm,kg=input().split()
cm,kg=int(cm),int(kg)
bmi=kg*(100**2)//(cm**2)
if bmi>=25:
    print(bmi,'Obesity',sep='\n')
else:
    print(bmi)