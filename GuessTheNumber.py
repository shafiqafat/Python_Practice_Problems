#This is a Guess the Number Game
import random
secretNumber = random.randint(1, 25)
print("I am thinking of a Number Between 1 to 25.")

#Asking the player to guess 5 times
for guessesTaken in range(1, 6):
    print("Take a guess :")
    guess = int(input())

    if guess > secretNumber:
        print("Your guess in too High.")
    elif guess < secretNumber:
        print("Your guess is too Low.")
    else:
        break            #Player Guessed it Right
if guess == secretNumber:
    print("Good Job!! You've Guessed the Number in just " +str(guessesTaken)+ " Guesses!!!")
else:
    print("You've Lost. The Number i was thinking of was " +str(secretNumber)+ ".Try Again???")
