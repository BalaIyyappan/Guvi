import random as r
g=('god','india','goa','books','king')
word = r.choice(g)
#print(word)
temp=[]
l=len(word)
i=0
while(i<10):
  guess=input("Enter any letter:")
  if guess in word:
    print("Your Guess is Correct")
    l=l-1
    temp.append(guess)
    if l==0:
      break
    print("You have",l,'more letters to Guess')
  else:
    print("You have",10-i,'chances and',l,"Letters")
  i=i+1

j="".join(temp)
#print(j)

if j==word:
  print("You Won!!")
else:
  print("You Lost. Game Over!")
