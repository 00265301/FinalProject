#Amanda Clooney 00265301                                                                                                                                                                #Amanda Clooney 00265301
#final project
#This program is a general knowledge quiz that will use various concepts from the semester

import random #import random to be used in question 15


x = random.randint(0, 9) #defines x as a random number
y = random.randint(0, 9) #defines y as a random number

#1- multiple choice
q1 = """What is the capital of Australia?\n1. Sydney\n2. Canberra\n3. Victoria\n4. Mackay""" #question 1 is assigned as q1 to put the answer in the dictionary
#2- multiple choice
q2 = """Which artist created the painting 'The Night Watch'?\n1. Leonardo da Vinci\n2. Salvador Dali\n3. Picasso\n4. Rembrant""" #question 2 is assigned as q2 to put the answer in the dictionary
#3- multiple choice
q3 = """How many elements are on the periodic table?\n1. 120\n2. 114\n3. 118\n4. 117""" #question 3 is assigned as q3 to put the answer in the dictionary
#4- multiple choice
q4 = """Who was the last member to join The Beatles?\n1. John\n2. Paul\n3. George\n4. Ringo""" #question 1 is assigned as q1 to put the answer in the dictionary
#5- multiple choice
q5 = """What is the northmost inhabited place on earth?\n1. Longyerbyden\n2. Barentsburg\n3. Dawson City\n4. Yellowknife""" #question 5 is assigned as q5 to put the answer in the dictionary
#6- multiple choice
q6 = """Who played Frankenstin in the 1931 film 'Frankenstein'?\n1. Boris Karloff\n2. Bela Lugosi\n3. Vincent Price\n4. Lon Chaney Jr.""" #question 6 is assigned as q6 to put the answer in the dictionary
#7- multiple choice
q7 = """What was the first Disney feature-lenght film?\n1. Bambi\n2. Snow White and the Seven Dwarves\n3. Dumbo\n4. Cinderella""" #question 7 is assigned as q7 to put the answer in the dictionary
#8- true/false
q8 = """Apollo 13 was the first mission with astronauts to land on the moon? True or False?""" #question 8 is assigned as q8 to put the answer in the dictionary
#9- user input
q9 = """What is 20 - 32?"""#question 9 is assigned as q9 to put the answer in the dictionary
#10- user input
q10 = """What is the name of the book by George Owell where the chracters are watched by big brother?"""#question 10 is assigned as q10 to put the answer in the dictionary
#11- user input
q11 = """What number does Roman numeral C stand for?""" #question 11 is assigned as q11 to put the answer in the dictionary
#12- user input
q12 = """What is the square root of 144?""" #question 12 is assigned as q12 to put the answer in the dictionary
#13- user input
q13 = """What is 8% of 30?""" #question 13 is assigned as q13 to put the answer in the dictionary

question = {q1:"2",q2:"4",q3:"3",q4:"4",q5:"1",q6:"1",q7:"2",q8:"false",q9:"-12",q10:"1984",q11:"100",q12:"12",q13:"2.4"} #dictionary

name = input("Hello, what is your name?\n")#user input 
print("Hello",name,"! You are about to take a general knowledge quiz.\nFor all questions requiring your input, please type in all lowercase.\nTry your best and your score will be calculated at the end!")
score = 0 #total variable
for i in question:
    print(i)
    answer = input("Answer:")
    if answer == question[i]: #if else string
        print("Correct!")
        score = score+1 #will add one to score if correct
    else:
        print("Wrong")
        score = score-0 #will cause score to not change if incorrect
        
#question 14 uses random numbers and is a multiplication operation
print("What is " + str(x), "*" + str(y)) #pulls two random numbers
q14 = int(input("Answer: "))
if q14 == (x * y): #if else
    print("Correct")
    score = score+1 #will add one to score if correct
else:
    print("Wrong")
    score = score-0 #will cause score to not change if incorrect

#question 15 will open the file "Alone" The user will then be able to read the poem and answer a question about it
file = open('Alone.txt', "r") #file will open
print(file.read()) #file will open on quiz 
print("In the poem 'Alone' by Edgar Allan Poe, what does the speaker compare the shapes of the clouds to?") #question 15
q15 = input("Answer: A ") #User input. I put "A " so the user can just type the word
if q15 == ("demon"): #Answer to question
    print("Correct")
    score = score+1 #will add one to score if correct
else:
    print("Wrong")
    score = score-0 #will cause score to not change if incorrect

    
print("Your total score is " + str(score) + " out of 15 \n") #score total
print("Thanks for playing {}! Bye!".format(name))
