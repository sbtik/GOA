my_num = 14

user_num1 = 0
user_num2 = 0

while user_num1 * user_num2 != my_num:
    user_num1 = int(input("Enter first number: "))
    user_num2 = int(input("Enter second number: "))

    if user_num1 * user_num2 != my_num:
        print("Incorrect!")

print("Correct!")