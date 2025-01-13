numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
my_index = 7
user_index = 0.1

while user_index != my_index:
    user_index = int(input("Enter Index: "))
    if user_index >= 31:
        print("ur index is mor 30")
    elif user_index != my_index:
        print("index is uncorect")

print("You Guessed Correctly!")