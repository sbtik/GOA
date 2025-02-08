numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers2 = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers2.append(numbers[i])
        print(numbers2)