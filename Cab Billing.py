usrname="bala"
pas="vbi"

i=3
while i!=0:
  u=input("Enter User Name:")
  p=input("Enter your Password:")
  if u==usrname:
    if p==pas:
      print("Welcome",usrname)
      loc=input("Enter your Location for pick up:")
      src=0
      dest=int(input("Enter your destination in KMS: "))
      total=dest-src
      car={'1':'Micro','2':'Sedan','3':'SUV','4':'Premium'}
      c=input("Select your car:1->Micro 2->Sedan 3->SUV 4->Premium: ")
      
      

      if car[c]=='Micro':
        t1={'1':'i10','2':'Tata indica','3':'Swift'}
        type1=input("Enter your choice:1->i10 2->Tata Indica 3->Swift: ")
        print("**************************")
        print("")
        print("$ Bill Details $       \n")
        print('Your Car is:',t1[type1])
        price1=10
        p1=(((total-5))*price1)
        if(total-5!=0):
          p1=p1+price1
        print("Your Car Type:",car[c])
        print('Total cost of travel:',p1)

      if car[c]=='Sedan':
        t2={'1':'Ciaz','2':'Verna','3':'Swift Desire'}
        type2=input("Enter your choice:1->Ciaz 2->Verna 3->Swift Desire: ")
        print("**************************")
        print("")
        print("$ Bill Details $  \n")
        print('Your Car is:',t2[type2])
        price2=15
        p2=(((total-5))*price2)
        if(total-5!=0):
          p2=p2+price2
        print("Your Car Type:",car[c])
        print('Total cost of travel:',p2)

      if car[c]=='SUV':
        t3={'1':'TUV 300','2':'Scorpio','3':'XUV 500'}
        type3=input("Enter your choice:1->TUV 300 2->Scorpio 3->XUV 500: ")
        print("**************************")
        print("")
        print("$ Bill Details $\n")
        print('Your Car is:',t3[type3])
        price3=20
        p3=(((total-5))*price3)
        if(total-5!=0):
          p3=p3+price3
        print("Your Car Type:",car[c])
        print('Total cost of travel:',p3)

      if car[c]=='Premium':
        t4={'1':'BMW 320d','2':'Audi A4','3':'Benz C class'}
        type4=input("Enter your choice:1->Bmw 320d 2->Audi A4 3->Benz C class: ")
        print("**************************")
        print("")
        print("$ Bill Details $\n")
        print('Your Car is:',t4[type4])
        price4=25
        p4=(((total-5))*price4)
        if(total-5!=0):
          p4=p4+price4
        print("Your Car Type:",car[c])
        print('Total cost of travel:',p4)
      
      break
    else:
      print("Password Incorrect!!")
  else:
    print("Invalid Username and password....Try Again!!!!")
  i=i-1
print("Have a nice Day!!")
