from random import randint
r=randint(0,10)
#print(r)
i=0
count=0
while(i<5):
  n=int(input("Enter any number within 10:"))
  if (n==r):
    print("Your Guess is correct ")
    print("!*************You Won************!")
    break
  else:
    print("Try Again")
    count=count+1
    if count==5:
      print("\nAll your Guesses are Wrong...\n:( You Lost The Game :(")
  i=i+1
