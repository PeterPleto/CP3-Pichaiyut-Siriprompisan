username = input("Username: ")
password = input("Password: ")
banana_price=20
apple_price=50
coffee_price=80
if username == "admin" and password == "pppp":
    print("Hello")
    print("Welcome")
    print("admin")
    print("Banana 20 baht")
    print("Apple 50 baht")
    print("Coffee 80 baht")
    userSelected = input("What do you want to buy? ")
    if userSelected== "banana":
        quantity = int(input("Quantity: "))
        print("Total Cost: ",banana_price*quantity)
        print("Have a nice day")
    elif userSelected== "apple":
        quantity = int(input("Quantity: "))
        print("Total Cost: ",apple_price*quantity)
        print("Have a nice day")
    elif userSelected== "coffee":
        quantity = int(input("Quantity: "))
        print("Total Cost: ",coffee_price*quantity)
        print("Have a nice day")
    else:
        print("error")
else:
    print("Login Failed")