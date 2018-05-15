#contacts list program

#create menu first

import sys #importing system function primarily the sys.exit() function

contacts = [] #initializing a list to store each contact in

class contact: #creating a class to store multiple items of information for each contact
    pass

############

def newContact():
    """function called in order to create a new contact"""
    
    newContact = contact() #assigns the class previously created to newContact

    newContact.name = input("Enter the contact's name: ") #asks for user input adds a name attribute to the class
    newContact.address = input("Enter the contact's address: ") #asks for user input adds a address attribute to the class
    newContact.number = input("Enter the contact's number: ") #asks for user input adds a number attribute to the class

    contacts.append(newContact) #adds the newContact, which is a contact() class to the contacts list
    print("New contact added") #testing to make sure the program is working up to this point
    main() #returns to the main menu

    #each of these fields would be saved as a whole object in the contacts list

##########

def findContact():
    """function called in order to search for a contact in the contacts list"""
    
    nameSearch = input("Please enter the name of the person you're looking for: ") #prompts user to enter in a full name
    for eachContact in contacts: #use a for loop to go through each object in the contacts list
        if eachContact.name == nameSearch: #if statement goes through if the user input matches the contact's name in the list
            print("Name:", eachContact.name) #response to the user, shows the found contact's name
            print("Address:", eachContact.address) #response to the user, shows the found contact's address
            print("Number:", eachContact.number) #response to the user, shows the found contact's phone number

            choice = input("Did you want to edit this contact? (y or n): ") #prompts the user if they want to edit the contact
            if choice == "n": #if statement goes through if the user chooses n, to go back to the main menu
                print("Returning to Main Menu.\n") #response to user for choosing "n"
                main() #program will go back to the main menu
            elif choice == "y": #elif statement if user chooses "y"
                print("Editing Contact.") #response to user for choosing "y"
                editContact(eachContact) #calls the editContact() function, including the contact that was found as an argument so it can be worked on in that function
        else: #else statement in case the name doesn't match the name in the list
            continue #this will return the program to the for loop, so it iterates to the next item in the list

    print("Could not find contact.") #will print out if the function goes through all the items in the list and does not find a match
    print("Returning to Main Menu.") #informing the user that the program is going back to the main menu
    main() #returning to the main menu

#######

def editContact(eachContact):
    """funciton called in order to edit a found contact.  takes the contact found as an argument"""
    
    print("Welcome to the Edit Menu") #prompts a user for a menu selection
    print("1. Change Name") #menu selection
    print("2. Change Address") #menu selection
    print("3. Change Number")#menu selection
    print("4. Nothing - Exit to Main Menu") #menu selection
    choice = input("What would you like to edit for this person? ") #prompts the user to make a menu selection

    if choice == "1": #if statement to match the user input
        newName = input("Enter new name: ") #prompts user to edit the name of the matched contact
        eachContact.name = newName #edits the contact's name
    elif choice == "2": #if statement to match the user input
        newAddress = input("Enter new Address: ") #prompts user to edit the name of the matched contact
        eachContact.address = newAddress #edits the contact's address
    elif choice == "3": #if statement to match the user input
        newNumber = input("Enter new Number: ") #prompts user to edit the name of the matched contact
        eachContact.number = newNumber #edits the contact's number
    else: #if user enters any other input
        main() #returns the program back to the main menu

##############

def mainMenu():
    """function called to display the main menu for the user"""
    
    print("Tiny Contacts\n\n") #title of the application
    print("1. New Contact")
    print("2. Find Contact")
    print("3. Exit Program\n")

    appOption = input("Enter your command: ") #prompts user for choice
    print("You chose: ", appOption) #informs user of choice

    return appOption #returns the user's choice out of the function as an integer

def main():
    """the primary function of the Tiny Contacts application"""
        selection = mainMenu() #reassigns the integer returned by the mainMenu() function

        if selection == "2": #if the user enters 2
            print("\nLooking for Contact.")
            findContact()

        elif selection == "1": #if the user enters 1
            print("\nCreating New Contact.")
            newContact()

        else: #if the user enters 3 or any other input
            print("\nExiting Program.")
            sys.exit()

###########

def saveContact():
    """define function to save contacts list in a text file"""
    pass

def loadContact():
    """define function to load contacts list from a text file"""
    pass
