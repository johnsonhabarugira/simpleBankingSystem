def shopping_cart():
    cart = []  # List to store the items in the cart
    print("Welcome to the Shopping Cart Program!")
    
    while True:
        print("\nOptions:")
        print("1. Add an item")
        print("2. Remove an item")
        print("3. View cart")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item = input("Enter the item to add: ")
            cart.append(item)
            print(f"{item} has been added to the cart.")
        
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item in cart:
                cart.remove(item)
                print(f"{item} has been removed from the cart.")
            else:
                print(f"{item} is not in the cart.")
        
        elif choice == '3':
            print("\nItems in your cart:")
            if not cart:
                print("Your cart is empty.")
            else:
                for i, item in enumerate(cart, 1):
                    print(f"{i}. {item}")
        
        elif choice == '4':
            print("Thank you for using the Shopping Cart Program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
shopping_cart()
