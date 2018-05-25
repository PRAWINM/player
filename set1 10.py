a,b=input().split(' ')
c=0
d=len(a)
for i in range(0,d):
  if(a[i]!=b[i]):
    c=c+1
if(c==1):
  print("yes")
else:
  print("no")
  
