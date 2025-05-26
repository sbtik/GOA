#მომხმარებელს შემოატანინეთ რიცხვი და შემდეგ კი დაბეჭდეთ ერთიდან ამ რიცხვამდე მხოლოდ ლუწი რიცხვების ჯამი ცალკე კენტის რიცხვების ჯამიც ცალკე

i3 = int(input("type your  odd number:"))
dirs =0
for i in range(i3):
    if i % 2 ==0:
        dirs = dirs + i
print( dirs)


i4 = int(input("type your even:"))
dirs =0
for i in range(i4):
    if i % 3 ==0:
        dirs = dirs + i
print( dirs)