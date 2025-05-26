cart = []
while True:
    actions = input("Add(a), Remove(r), Submit(s): ")
    if actions == "a":
        product = input("Products: ")
        cart.append(product)
        
    elif actions == "r":
        product = input("Enter wich one do you want to remove: ")
        if product in cart:
            cart.remove(product)
        else:
            print("product not found")

    elif actions == "s":
        break
    else:
        print("try again ")
print(cart)

            


    
    

