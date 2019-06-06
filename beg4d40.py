#monisha
n=int(input())
first=0
sec=1
for i in range(n):
	print(sec,end=" ")
	temp=first
	first=sec
	sec=temp+sec
 
