age = int(input("Enter the age: "))

if 18 <= age < 50:
    print("The age is between 18 and 50.")
elif age < 18 or age > 50:
    print("They must be either elderly or young.")
else:
    print("Not in the specified age category.")
