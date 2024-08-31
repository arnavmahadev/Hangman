import random
print ("Let's play hangman!")
ansIndex = random.randint(0, 7)
list = ["protein", "secret", "white", "discombobulation", "shampoo", "blanket", "kettle", "football"]
ans = list[ansIndex]
for x in range(0, len(ans)):
    print ("_", end = " ")
print ("\nThe answer has " + str(len(ans)) + " letters!")
lives = 10
correct = []
while lives > 0:
    guess = input("Guess a letter: ")
    if guess in ans:
        correct.append(guess)
    else:
        lives -= 1
        print("INCORRECT! \nLives Remaining: " + str(lives))
    for letter in ans:
        if letter in correct:
            print (letter, end = " ")
        else:
            print ("_", end = " ")
    if all(letter in correct for letter in ans):
        print("\nCongratulations, you guessed the word!")
        break
else:
    print ("Game Over! \nThe correct answer was " + ans)