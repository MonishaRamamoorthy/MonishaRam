#monisha
a=int(input())
s=0
temp=a
while(a>0):
    rem=a%10
    s=s+(rem**3)
    a=a/10
    a=int(a)
if(s==temp):
    print("yes")
else:
    print("no")
