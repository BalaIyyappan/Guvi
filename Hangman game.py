import random as r
g=('god','india','goa','books','king')
word = r.choice(g)
#print(word)
temp=[]

print("******Let's Play Hangman******")
l=len(word)
for i in range(l):
  print("_",end=" ")
print("\n\nGuess The Word\n")
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

if l==0:
  print("\nYou Won!!")
else:
  print("\nYou Lost. Game Over!")
