numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = 0

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
       odd_numbers += numbers[i]
 
print(odd_numbers)