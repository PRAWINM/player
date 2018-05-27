n=input("Enter the string:")
c=('a','e','i','o','u','A','E','I','O','U')
a=[]
for i in n:
  if i in c:
    continue
  else:
    a.append(i)
b=a[::-1]
print(''.join(b))
