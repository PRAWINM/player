N,K=map(int,input().split(" "))
L=list(map(int,input().split(" ")))[:N]
del L[-K:]
print(L)
