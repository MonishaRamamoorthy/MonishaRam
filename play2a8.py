#monisha
num=int(input())
l=[]
c=0
kr="kabali"
a=sorted(kr)
for i in range(num):
	s=input()
	l.append(s)
for i in l:
	if sorted(i)==a:
		c=c+1
print(c)
