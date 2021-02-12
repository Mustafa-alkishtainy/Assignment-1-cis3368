##Mustafa Al-kishtainy
##professor Otoo 3368


id=""
contactDetail=""
creationDate=""


def Menu():
    print("Menu: ")
    print("a - Add contact")
    print("d - Delete contact")
    print("u - Update contact")
    print("b - Output all contacts in alphabetical order")
    print("c - Output all contacts by creation date")
    print("q - Quit")

Menu()
choice = input("Choose an option: ")

while choice != 'q':
    if choice == 'a':
        id= input("Enter user ID: ")
        contactDetail= input("Enter contact details: ")
        creationDate = input("On what date was this document created?:")
    elif choice == 'd':
        print('d')
    elif choice == 'u':
        print('u')
    elif choice == 'b':
        print('b')
    elif choice == 'c':
        print('c')
    else: 
        print("invalid")
    
    
    print()
    Menu()
    choice = input("Choose an option: ")

    





