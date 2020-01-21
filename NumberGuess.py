from random import randint
r=randint(0,10)
#print(r)
i=0
while(i<5):
  n=int(input("Enter any number within 10:"))
  if (n==r):
    print("Your Guess is correct ")
    print("!*************ou Won************1")
    break
  else:
    print("Try Again")
  i=i+1
