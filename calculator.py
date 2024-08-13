firstnumber= int(input("Enter your first number:"))
operator = input("Enter your operator +,-,*,/:")
secondnumber= int(input("Enter your second number:"))
if operator == "+":
    print(firstnumber + secondnumber)

elif operator == '-':
    print(secondnumber-firstnumber)

elif operator == '*':
    print(firstnumber*secondnumber)
elif operator == '/':
     print(firstnumber/secondnumber)
else:
    print("Invalid operator")