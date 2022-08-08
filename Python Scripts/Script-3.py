# importing the module
import sys


def load():
    l1 = []
    # open the file for reading
    with open("contacts.txt", "r") as fn:
        # for each line in the file
        for line in fn:
            l2 = []
            # read the line as a colon separated list
            line = line.split(':')
            # the name is the first list item
            # name = line[0]
            l2.append(line[0])
            # phone = []
            if len(line) == 2:
                l2.append(int(line[1]))
            elif len(line) == 3:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
            elif len(line) == 4:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
            elif len(line) == 5:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
                l2.append(int(line[4]))
            elif len(line) == 6:
                l2.append(int(line[1]))
                l2.append(int(line[2]))
                l2.append(int(line[3]))
                l2.append(int(line[4]))
                l2.append(int(line[5]))
            l1.append(l2)

    return l1


def menu():
    # We created this simple menu function for
    # code re usability & also for an interactive console
    # Menu func will only execute when called
    print("\n************************")
    print("\t\t\tPHONE DIRECTORY", flush=False)
    print("************************")
    print("\tYou can now perform the following operations on this phonebook\n")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")

    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6
    # We return the entered choice to the calling function wiz main in our case
    choice = int(input("Please enter your choice: "))
    print("\n")
    return choice

# this function displays all content of phonebook pb


def display_all(pba):
    if not pba:
        # if display function is called after deleting all contacts then the len will be 0
        # And then without this condition it will throw an error
        print("Contacts is empty...")
    else:
        pba.sort()
        for i in range(len(pba)):
            print(pba[i])
    print("\n")


def add_contact(apb):
    # Adding a contact is the easiest because all you need to do is:
    # append another list of details into the already existing list
    enter = int(input("How Many contacts do you want to enter : "))
    # dip.clear()
    for i in range(0, enter):
        dip = []
        dip.append(str(input("Enter name: ")))
	#we assume that 1 person has maximum 5 contacts...
        enter_con = int(
            input("How many contacts numbers you want to add(maximum 5 contacts): "))
        for j in range(0, enter_con):
            num = input("Enter Contact number: ")
            dip.append(num)
        apb.append(dip)
    return apb


def remove_existing(bpb):
    # This function is to remove a contact's details from existing phonebook
    query = str(
        input("Please enter the name of the contact you wish to remove: "))
    # We'll collect name of the contact and search if it exists in our phonebook

    temp = 0
    # temp is a checking variable here. We assigned a value 0 to temp.

    for i in range(len(bpb)):
        if query == bpb[i][0]:
            temp += 1
            # Temp will be incremented & it won't be 0 anymore in this function's scope

            print(bpb.pop(i))
            # The pop function removes entry at index i

            print("This query has now been removed")
            # printing a confirmation message after removal.
            # This ensures that removal was successful.
            # After removal we will return the modified phonebook to the calling function
            # which is main in our program
            return bpb

    if temp == 0:
        # Now if at all any case matches temp should've incremented but if otherwise,
        # temp will remain 0 and that means the query does not exist in this phonebook
        print("Sorry, you have entered an invalid query.\
    Please recheck and try again later.")

    return bpb


def delete_all(cpb):
    # This function will simply delete all the entries in the phonebook pb
    # It will return an empty phonebook after clearing
    with open("contact2.txt", 'w') as f:
        pass
    return cpb.clear()


def search_contact(dpb):
    # This function searches for an existing contact and displays the result
    # choice = str(input("Enter search Keyword : "))
    # We're doing so just to ensure that the user experiences a customized search result

    temp = []
    check = -1
    query = str(
        input("Please enter the name/keyword of the contact you want to search: "))
    for i in range(len(dpb)):
        if query in dpb[i][0]:
            check = i
            temp.append(dpb[i])

    if check == -1:
        print("The contact does not exist. Please try again\n")
    # If the user enters any other choice then the search will be unsuccessful
    # print("Invalid search criteria")
    # return -1
    # returning -1 indicates that the search was unsuccessful

    # all the searches are stored in temp and all the results will be displayed with
    # the help of display function
    else:
        display_all(temp)
    # return check


def thanks(rpb):
    rpb.sort()

    with open("contacts.txt", 'w') as fn:
        for i in range(len(rpb)):
            for j in range(len(rpb[i])-1):
                fn.write(str(rpb[i][j]))
                fn.write(":")
            fn.write(str(rpb[i][len(rpb[i])-1]) + "\n")

    # A simple gesture of courtesy towards the user to enhance user experience
    print("\n************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("************************")
    sys.exit("Goodbye, have a nice day ahead!\n")


# Main function code
print("\n....................................................................")
print("Hello User, Welcome To Our Phone Directory System")
print("You may now proceed to explore this directory")
print("....................................................................")
# This is solely meant for decoration purpose only.
# You're free to modify your interface as per your will to make it look interactive

ch = 1
pb = load()  # initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu()
    if ch == 1:
        pb = add_contact(pb)
    elif ch == 2:
        pb = remove_existing(pb)
    elif ch == 3:
        pb = delete_all(pb)
    elif ch == 4:
        search_contact(pb)
    # if d == -1:
    #     print("The contact does not exist. Please try again")
    elif ch == 5:
        display_all(pb)
    else:
        thanks(pb)
