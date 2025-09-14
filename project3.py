contacts = {}

print('\n********Contact list********')
print('1. Add number')
print('2. Update number')
print('3. Delete number')
print('4. View numbers')
print('5. Exit')

while True:
    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter a contact name: ")
        if name in contacts:
            print(f"the name {name} already exist! ")
        else:
            first_name = input("Enter first name:")
            last_name = input("Enter last name:")
            phone_no = input("Enter phone number:")
            contacts[name] = {'first_name': first_name,
                              'last_name': last_name, 'phone_no': phone_no}
            print(f'The new contact {name} is added!')

    elif choice == '2':
        name = input("Enter a  contact name to update: ")
        if name in contacts:
            first_name = input("Enter updated first name:")
            last_name = input("Enter updated last name:")
            phone_no = input("Enter updated phone number:")
            contacts[name] = {'first_name': first_name,
                              'last_name': last_name, 'phone_no': phone_no}
            print(f'The  contact {name} is updated!')

        else:
            print('Contact does not exist!')

    elif choice == '3':
        name = input("Enter a contact name: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted!")

        else:
            print(f"Contact {name} does not exist!")

    elif choice == '4':
        if not contacts:
            print("No contacts found.")
        else:
            print("\n******* All Contacts *******")
            i = 1
            for name, info in contacts.items():
                print(f"\nContact #{i}")
                print(f"Name      : {name}")
                print(f"First Name: {info['first_name']}")
                print(f"Last Name : {info['last_name']}")
                print(f"Phone No  : {info['phone_no']}")
                i += 1

    elif choice == '5':
        print('GoodBye')
        break

    else:
        print("wrong option")
