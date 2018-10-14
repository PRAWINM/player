L,R=map(int,input().split(" "))
sum=0
for i in range(L,R+1):
  if(i%2!=0):
    sum=sum+i
print(sum)
