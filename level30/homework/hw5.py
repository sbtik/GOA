numbers = [13, 12, 43, 54, 65, 16, 67, 98, 19, 910]
resultad = []
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        resultad.append(numbers[i])
print(resultad)