#number = int(input("Enter your number: "))
#if number<=1:
 #   print("Not prime")

num = int(input("Enter your number: "))
for i in range(2, num):
    if num % i == 0:
        print(f"{num} is not a prime number")
    break
else:
    print(f"{num} is a prime number")
