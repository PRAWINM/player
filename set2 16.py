N=int(input())
L=list(map(int,input().split(" ")))[:N]
A=[]
for i in L:
  if(L.count(i)!=1):
    continue
  else:
    A.append(i)
print(''.join(str(x) for x in A))
