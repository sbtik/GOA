numbers = [1,2,3,4,5,6,7,8,10,124236534]

max_numbers = numbers[0]

for number in numbers:
    if number < max_numbers:
        max_numbers = number
print(max_numbers)