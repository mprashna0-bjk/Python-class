'''
Exercise 20: Simple contact book menu-deiven contact book using a dictionary
'''
contacts = {
"Ram": "9841000000",
"Sita": "9851000000",
"Hari": "9861000000"
}

while True:
    print("\n===== contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4 Delete Conatact")
    print("5. Display Contacts")
    print("6. Exit")
    choice = int(input("Eenter your choice:"))
    if choice ==1:
        name = input("Enter name:")
        number = input ("Enter phone number:")
        contacts[name] = number 
    elif choice == 2:
        name = input("Enter contact name:")
        if name in contacts:
            print(name, ":", contacts[name])
        else:
            print("Contact not found.")
    elif choice == 3:
        name = input ("enter contact name: ")
        if name in contacts:
            contacts[name] = input("Enter new number:")
            print("Contact updated.")
        else: 
            print("contact not found.")
    elif choice == 4: 
        name = input ("enter contact name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == 5:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(name, ":", number)
    elif choice == 6:
        print("Existing contact Book..")
        break 

    else:
        print("Invalid Choice!")


    
        