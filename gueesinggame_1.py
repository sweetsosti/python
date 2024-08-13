import random
random_number = random.randint(1,100)
print("Welcome to the game of guessing number")

attempt =1
max_attempt =6
print("You have 6 attempt to guess the number")

while attempt <=max_attempt:
 guess = int(input("Guess a number between 1 and 100: "))
 if guess == random_number:
    print(f"Yay! you have guessed the number {random_number} in {attempt}")
    break
 elif guess >random_number:
    print(f"{guess} number is too high!, and you have {max_attempt-attempt} attempt left")
 elif guess <random_number:
    print(f"{guess} number is too low!, and you have {max_attempt-attempt} attempt left")

attempt +=1

if attempt <max_attempt:
    print(f"Sorry you did not guess it, the number was {random_number}")
