import random
random_number = random.randint(1,100)
attempt =1
max_attempt =6
print("You have 6 attempts to guess number")

while attempt <=max_attempt:
    guess = int(input("Guess the number between 1 to 100: "))
    if guess == random_number:
        print(f"Congratulations you guess it on {attempt} attempt")
        break
    elif guess >random_number:
        print(f"Guess lower number and you have {max_attempt-attempt} attempt left")
    elif guess <random_number:
        print(f"Guess higher number and you have {max_attempt-attempt} attempt left")
    
    attempt +=1

    if attempt > max_attempt:
        print(f"Sorry you didn't guess it, the number was {random_number}")