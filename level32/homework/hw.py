numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_list = []
i = len(numbers) - 1
while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1
print(reversed_list)