num,power=map(int,input().split(' '))
while(num%power==0):
    num/=power
if(num==1):
    print('yes')
else:
    print('no')
