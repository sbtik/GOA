#8) შექმენით input  რომელიც მომხმარებელს ეკითხება რიცხვს და შემდეგ while  ციკლის გამოყენებით ი დაიწყებს რიცხვების დაბეჭდვსს სანამ არ მიაღწევს ნულს

number =int(input("whats your number"))
while  number <= 100:
    
    print(number)
    number = number - 1
    if number <=0:
        number = number + 101