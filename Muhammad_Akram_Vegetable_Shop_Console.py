# Muhammad Akram Vegetable Shop Chatbot (Console Version)

vegetables = {
    "potato": 80,
    "tomato": 120,
    "onion": 100,
    "carrot": 150,
    "cabbage": 90
}

print("="*50)
print("   Welcome to Muhammad Akram Vegetable Shop")
print("="*50)

while True:
    print("\n1. Show Price List")
    print("2. Check Vegetable Price")
    print("3. Buy Vegetables")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nPrice List")
        for v,p in vegetables.items():
            print(f"{v.title():10} : Rs.{p}/kg")

    elif choice == "2":
        name = input("Enter vegetable name: ").lower()
        if name in vegetables:
            print(f"{name.title()} = Rs.{vegetables[name]}/kg")
        else:
            print("Sorry! Vegetable not available.")

    elif choice == "3":
        name = input("Vegetable name: ").lower()
        if name in vegetables:
            kg = float(input("Quantity (kg): "))
            total = kg * vegetables[name]
            print(f"Total Bill = Rs.{total:.2f}")
            print("Thank you for shopping!")
        else:
            print("Vegetable not available.")

    elif choice == "4":
        print("Thank you for visiting Muhammad Akram Vegetable Shop!")
        break

    else:
        print("Invalid choice. Try again.")
