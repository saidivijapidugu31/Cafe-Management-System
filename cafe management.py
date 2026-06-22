menu = {
    "Tea": 10,
    "Coffee": 20,
    "Burger": 50,
    "Pizza": 100
}

print("===== CAFE MENU =====")
for item, price in menu.items():
    print(item, "-", price)

total = 0

while True:
    item = input("Enter item name: ")

    if item in menu:
        total += menu[item]
        print(item, "added")
    else:
        print("Item not available")

    choice = input("Add another item? (yes/no): ")

    if choice.lower() == "no":
        break

print("Total Bill =", total)
print("Thank You Visit Again!")
