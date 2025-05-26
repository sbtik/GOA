number= int(input("მომე რიცხვი: "))


i1 = 0
i2 = 0
i = 1
while i <= number:
    if i % 5 == 0:
        i1 += i 
    if i % 3 == 0:
        i2 += i 
    i += 1  
print(i1)
print(i2)