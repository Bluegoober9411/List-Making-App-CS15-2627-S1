shopping_list = []
previous_list = []

while True:
    print("\nShopping List Menu")
    print("1. Add an Item")
    print("2. Remove an Item")
    print("3. Display the List")
    print("4. Undo the Previous Change")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        previous_list = shopping_list.copy()
        item = input("Enter an item to add: ")
        shopping_list.append(item)
        print(item, "was added.")

    elif choice == "2":
        if len(shopping_list) == 0:
            print("The shopping list is empty.")
        else:
            previous_list = shopping_list.copy()

            print("\nShopping List:")
            for i in range(len(shopping_list)):
                print(i, "-", shopping_list[i])

            index = int(input("Enter the index of the item to remove: "))

            if index >= 0 and index < len(shopping_list):
                removed_item = shopping_list.pop(index)
                print(removed_item, "was removed.")
            else:
                print("Invalid index.")

    elif choice == "3":
        if len(shopping_list) == 0:
            print("The shopping list is empty.")
        else:
            print("\nShopping List:")
            for item in shopping_list:
                print("-", item)

    elif choice == "4":
        shopping_list = previous_list.copy()
        print("The previous change has been undone.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")