#monisha
m=int(input())
if(m<=1000):
  n=list(map(int,input().split(" ")))
  i=len(n)//2
  n.sort()
  print(n[i])
