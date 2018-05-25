N=int(input())
L=[]
for i in range(0,N):
  c=input()
  L.append(c)
L.sort(key=len)
print(" ".join(L))
