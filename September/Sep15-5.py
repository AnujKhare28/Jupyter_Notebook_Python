print("Welcome to the Quiz!")
playing = input("Do you want to play (y/n)? ")
score = 0

if playing.lower() == 'n': 
    quit()

print("Let's start!!")

ans1 = input("1. What does CPU stand for? ")
if ans1 == 'Central Processing Unit':
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("Correct answer: Central Processing Unit")
    score -= 1

ans2 = input("2. What is the capital of Russia? ")
if ans2 == 'Moscow':
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("Correct answer: Moscow")
    score -= 1

ans3 = input("3. Who discovered zero (0)? ")
if ans3 == 'Aryabhatt':
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("Correct answer: Aryabhatt")
    score -= 1

ans4 = input("4. ISRO stands for? ")
if ans4 == 'Indian Space Research Organisation':
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("Correct answer: Indian Space Research Organisation")
    score -= 1

ans5 = input("5. Heat is which type of energy? ")
if ans5 == 'Radiation':
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")
    print("Correct answer: Radiation")
    score -= 1

print("Score:", score)
print("Thank you for playing :)")