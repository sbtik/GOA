numbers = [5, 15, 48, 44, 32, 64, 72, 8, 14, 20]
for i in range(len(numbers)):
    if numbers[i] % 5 == 0:
        print(numbers[i], "ხუტის ჟერადია")
    elif numbers[i] % 3 == 0:
        print(numbers[i], "სამის ჯერადია")