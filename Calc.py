def a(n1,n2):
  
  return n1+n2

def s(n1,n2):
  
  return n1-n2

def m(n1,n2):
  
  return n1*n2

def d(n1,n2):
  
  if n2==0:
    print("Division by Zero is not allowed")
  else:
    return n1/n2

def calc(i,n1,n2):


  if i==1:
    print("Addition Value is",a(n1,n2))
  elif i==2:
    print("Subtraction value is",s(n1,n2))
  elif i==3:
    print("Multiplication value is",m(n1,n2))
  elif i==4:
    print("Division Value is",d(n1,n2))
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

def numbers():
  print("NUMBERS\n")
  print("1\t2\t3\t\n4\t5\t6\t\n7\t8\t9\t\n\t0")

def start():
  c='y'
  while(c=='y'):
    n1=int(input("Enter 1st number:"))
    n2=int(input("Enter 2nd number:"))
    print("What would you like to do:")
    print('1:Add 2:Sub 3:Mul 4:Div')
    i=float(input("Enter Your Choice: "))
    if (i<=4):
      calc(i,n1,n2)
    else:
      abn()
    c=input()

numbers()
start()
