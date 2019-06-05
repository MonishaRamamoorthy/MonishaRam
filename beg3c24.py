#monisha 
m=int(input())
if(m<=100):
  n=list(map(int,input().split()))
  n.sort()
  print(*n)
