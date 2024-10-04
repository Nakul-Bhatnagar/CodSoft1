#-----------------------------------------------------------------------------------------------------------#
#----------------------------------------------- CONTACT BOOK ----------------------------------------------#

def display_menu():
    print("\n...Welcome to the Contact Book !...")
    print("\n1 - Feed a New Contact")
    print("2 - Search Contact by Name")
    print("3 - Delete Contact")
    print("4 - Show All Contacts")
    print("5 - Exit")
    option = int(input("\nChoose your option : "))
    return option

def add_contact(contact_details):

    print("\nAdd New Contact ")
    contact = []
    name=str(input("Enter Name: "))
    num=str(input("Enter Mobile Number: "))
    mail=str(input("Enter Email_ID: "))
    address=str(input("Enter Address: "))
    contact.append(name)
    contact.append(num)
    contact.append(mail)
    contact.append(address)
    contact_details.append(contact)
    print("Contact added successfully ..!")
    


def search_contact(contact_details):
    name = input("\nEnter the Name to search: ")
    found = False
    for contact in contact_details:
        if contact[0]== name:
            print("\nContact found!")
            display_contact(contact)
            found = True
    if not found:
        print("No contact found with the name", name)

    

def delete_contact(contact_details):
    name = input("\nEnter Name of the contact to be deleted : ")

    for i, contact in enumerate(contact_details):
        if contact[0] == name:
            print("\nDeleting the following contact:")
            print(contact)
            del contact_details[i]
            print("Contact deleted successfully!")
            return
    print("No contact found with the name", name)


def display_all_contacts(contact_details):
    if len(contact_details) == 0:
        print("\nNo contacts available to display ...")
    else:
        print("\nAll Contacts : ")
        for contact in contact_details:
            display_contact(contact)


def display_contact(contact):
    print("Name : ",contact[0])
    print("Mob_Number : ",contact[1])
    print("Mail_ID : ",contact[2])
    print("Address : ",contact[3])
    print("-" * 30)


def main():
    contact_details=[
        ["Aman Singh","123456","aman@gmail.com","South Delhi"],
        ["Kavya Nair","789101","knair@gmail.com","Lucknow,UP"]
    ]

    while True:
        option = display_menu()

        if option == 1:
            add_contact(contact_details)
        elif option == 2:
            search_contact(contact_details)
        elif option == 3:
            delete_contact(contact_details)
        elif option == 4:
            display_all_contacts(contact_details)
        elif option == 5:
            print("Exiting the Address Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()
