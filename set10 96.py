N=int(input())
N1=N%10
N2=N
while(N2>=10):
  N2=N2//10
print(N1+N2)
