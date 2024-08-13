#WAP to take user input email and validate wether it is correct email or not

#while True:
 #  email = input("Enter your email address: ")

#if '@' not in email or '.com' not in email:
     # print("Not a valid email. Please try again.")
    #break

   #else:
    #  print("Valid email.")
      

#WAP to take user input mark percentage and find their division.

name = input("enter your good name:")
percentage= int(input("Please enter your percentage to know your division:-"))

if percentage > 100 or percentage < 0:
    print("Percentage must be between 0 and 100.")
elif percentage >= 80:
    print(f"Congratulations, {name}! You scored Distinction.")
elif percentage >= 60:
    print(f"Congratulations, {name}! You scored First Division.")
elif percentage >= 50:
    print(f"Congratulations, {name}! You scored Second Division.")
elif percentage >= 40:
    print(f"Congratulations, {name}! You scored Third Division.")
else:
    print("Sorry, you are fail.")
