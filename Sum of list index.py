i=int(input())
l=[]
for j in range(i):
  a=int(input())
  l.append(a)
print(l)
ind=int(input("Enter Index Value:"))
e=0
o=0
even=[]
odd=[]
for k in range(0,ind+1):
  if(l[k]%2==0):
    e=e+l[k]
    even.append(e)
  else:
    o=o+l[k]
    odd.append(e)

print("Odd list",o)
print("Even List",e)
