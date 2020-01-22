c=0
for i in range(1,100,2):
  if c!=20:
    print(i,end=" ")
    c=c+1
  else:
    break
    
c=0
for i in range(2,100,2):
  if c!=20:
    print(i,end=" ")
    c=c+1
  else:
    break
    
c=0
for i in range(1,100,2):
  if c!=20:
    print(i**2,end=" ")
    c=c+1
  else:
    break
    
c=0
for i in range(2,100,2):
  if c!=20:
    print(i**2,end=" ")
    c=c+1
  else:
    break
    
c=0
for i in range(2,100,2):
  if c!=20:
    if i%2==0:
      print(i*2,end=" ")
      c=c+1
    else:
      print(i,end=" ")
  else:
    break
    
    
c=0
for i in range(1,100):
  if c!=20:
    if i%2==0:
      print(i*2,end=" ")
    else:
      print(i,end=" ")
    c=c+1
  else:
    break
    
c=0
for i in range(1,100):
  if c!=20:
    if i%2!=0:
      print(i**3,end=" ")
    else:
      print(i,end=" ")
    c=c+1
  else:
    break
