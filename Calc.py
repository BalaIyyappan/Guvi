def a():
  n1=int(input("Enter 1st number:"))
  n2=int(input("Enter 2nd number:"))
  return n1+n2

def s():
  n1=int(input("Enter 1st number:"))
  n2=int(input("Enter 2nd number:"))
  return n1-n2

def m():
  n1=int(input("Enter 1st number:"))
  n2=int(input("Enter 2nd number:"))
  return n1*n2

def d():
  n1=int(input("Enter 1st number:"))
  n2=int(input("Enter 2nd number:"))
  return n1/n2



c='y'
while(c=='y'):
  print("What would you like to do:")
  print('1:Add 2:Sub 3:Mul 4:Div')

  i=int(input("Enter Your Choice: "))
  if i==1:
    print("Addition Value is",a())
  if i==2:
    print("Subtraction value is",s())
  if i==3:
    print("Multiplication value is",m())
  if i==4:
    print("Dicision Value is",d())
  print("If you want to continue: Press Y or N:")
  c=input()
