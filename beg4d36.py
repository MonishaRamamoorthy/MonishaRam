#monisha
x=input()
count=0
for i in x:
	if(i.isnumeric()!=True and i.isalpha()!=True):
		count=count+1
print(count)		
