
import random
#print("welcome to the guessing game")
#print("you have 3 tries to get it correct. ")

'''for attempt in range(1,4):
    guess = int(input(f"this is guess # {attempt}: "))
    

    if guess == 4:
        print("congratulations")
        break
    if attempt < 3:
                print("try again")
    else:
        print("game over")'''
#. it should show number of tries taken to guess the correct number
# Add the amount of tries 


print("welcome to the guessing game")
tries = int(input ("How many tries would you like to have?"))

print(f"you have {tries} tries to get it correct. ")

attempt = 0
correctnum = random.randrange(1,11)
while attempt < tries:
    
    guess = int(input(f"this is guess # {attempt+1}: "))
    attempt += 1
    if guess == correctnum:

        print(f"congratulations, you completed it in {attempt} tries!")
        break
    elif attempt < tries:
        print("try again:")
    else:
        print("Game Over.")



