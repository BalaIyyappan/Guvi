x = 0
score = x
print("Welcome To Quiz Game!!\n")

question=["How many wings does a swan has?","Who is the president of the United States?","Australian Currency is Australian Dollar?","Who was the last year winner of IPL?",
"True or False... The current Prime Minister of India is Narendra Modi?"]

print(question[0])
answer_1 = input("a)1 b)2 c)3 d)4:")
if answer_1.lower() == "b" or answer_1.lower() == "2":
    print("Correct")
    x = x + 1   
else:
    print("Incorrect, 1 + 1 is 2")


print(question[1])
answer_2 = input("a)Barack Obama b)Hillary Clinton c)Donald Trump d)Tom Brady:")
if answer_2.lower() == "c" or answer_2.lower() == "donald trump":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The president is Donald Trump")


print(question[2])
answer_3 = input("Is it True?(T/F):")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    print("Correct")
    x = x + 1
else:
     print("Incorrect")  


print(question[3])
answer_4 = input("a)CSK b)MI c)RCB d)KKR:")
if answer_4.lower() == "b" or answer_4 == "MI":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The last year IPL winner is Mumbai")


print(question[4])
answer_5 = input("(True/False):")
if answer_5.lower() == "True" or answer_5.lower() == "t":
    print("Correct")
    x = x + 1
else:
    print("Incorrect, The current Prime Minster of India is Modi")



score = float(x / 5) * 100
print(x,"out of 5, You scores",score, "%")
