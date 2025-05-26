PC_PARTS_SHOP = []
while True:

    actions = input("Add(a), Remove(r), Submit(s): ")
    if actions == "a":
        product = input("Parts: ")
        PC_PARTS_SHOP.append(Part)
        
    elif actions == "r":
        Part = input("Enter wich one do you want to remove: ")
        if product in PC_PARTS_SHOP:
            PC_PARTS_SHOP.remove(product)
        else:
            print("Part is not found")

    elif actions == "s":
        break
    else:
        print("try again and again ")
print(PC_PARTS_SHOP)
