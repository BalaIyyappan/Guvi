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
  if n2==0:
    print("Division by Zero is not allowed")
  else:
    return n1/n2

def calc(i):


  if i==1:
    print("Addition Value is",a())
  elif i==2:
    print("Subtraction value is",s())
  elif i==3:
    print("Multiplication value is",m())
  elif i==4:
    print("Dicision Value is",d())
  else:
    print("Kindly Enter a valid choice")
    start()
  p=input("If you want to continue: Press Y or N:")
  if(p=='y' or p=='Y'):
    start()
  else:
    abn()
    
def abn():
  print("Thank You!! Seems You Don't need Calculator Genius ")   
  exit 


def start():
  c='y'
  while(c=='y'):
    print("What would you like to do:")
    print('1:Add 2:Sub 3:Mul 4:Div')
    i=float(input("Enter Your Choice: "))
    if (i==1 or i==2 or i==3 or i==4):
      calc(i)
    else:
      abn()
    c=input()

start()
