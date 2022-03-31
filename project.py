import random
randNo = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNo):
    userGuess = int(input("Enter your Guess: "))
    guesses += 1
    if (userGuess == randNo):
      print("Conrats! You Guessed it RIGHT!")

    else:
        if (userGuess>randNo):
         print("OOPS! You Guessed it WRONG! Try smaller number") 
        
        else:
         print("OOPS! You Guessed it WRONG! Try larger number")

print(f"You guessed it right in {guesses} guesses")

# with open("highscore.txt" , "r") as f:
#      highscore=int(f.read())

# if (guesses<highscore):
#     print("You have just broken the Highscore!")
#     with open("highscore.txt" , "w") as f:
#      f.write(str(guesses))

