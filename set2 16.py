N=int(input())
L=[]
for i in range(0,N):
  c=int(input())
  L.append(c)
A=[]
for i in L:
  if(L.count(i)!=1):
    continue
  else:
    A.append(i)
print(''.join(str(x) for x in A))
