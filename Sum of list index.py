i=int(input())
l=[]
for j in range(i):
  a=int(input())
  l.append(a)
print(l)
ind=int(input("Enter Index Value:"))
s=0

for k in range(0,ind+1):
  s=s+l[k]
print(s)
l.append(s)
print(l)
