#contacts list program

#create menu first

import sys

contacts = []

class contact:
    pass

############

def newContact():
    newContact = contact()

    newContact.name = input("Enter the contact's name: ")
    newContact.address = input("Enter the contact's address: ")
    newContact.number = input("Enter the contact's number: ")

    contacts.append(newContact) #adds the newContact to the contacts list
    print("New contact added")
    main()

    #each of these fields would be saved as a whole object in the contacts list

##########

def findContact():
    """implement findContact() function here"""
    #prompt user to enter in a full name
    nameSearch = input("Please enter the name of the person you're looking for: ")
    #use a for loop to go through each object in the contacts list
    for eachContact in contacts:
        if eachContact.name == nameSearch:
            print("Name:", eachContact.name)
            print("Address:", eachContact.address)
            print("Number:", eachContact.number)
            main()
        else:
            continue

    print("Person is not in the directory.\n")
    main()

##############

def mainMenu():
    print("Tiny Contacts\n\n") #title of the application
    print("1. New Contact")
    print("2. Find Contact")
    print("3. Exit Program\n")

    appOption = input("Enter your command: ")
    print("You chose: ", appOption)

    return appOption

def main():
        selection = mainMenu()

        if selection == "2":
            print("\nLooking for Contact.")
            findContact()

        elif selection == "1":
            print("\nCreating New Contact.")
            newContact()

        else:
            print("\nExiting Program.")
            sys.exit()

###########
