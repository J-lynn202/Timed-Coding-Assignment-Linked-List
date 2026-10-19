from linked_list import Linkedlist

def main():
    Clients = Linkedlist()

    while True:
     print("\nBoudreaux's BarberShop")
     print("Type the number for the action you wish to perform and then hit Enter")
     print("1. Add a new client") 
     print("2.Display a list of all current clients")
     print("3. Search for a client")
     print("4.Delete a client")
     print("5. Quit")

    choice = input ("\nWhat do you want to do? ")

if choice =="1":
    print("\n Type the number for the action you wish to perform and then hit Enter")
    name = input("Provide Client's name: ")
    phone = input("Provide Client'sPhone number: ")
    dob = input("Provide Client's D.O.B in MMDDYYYY: ")

    Clients.add_client(name, phone, dob)

elif choice == "2": 
    clients.display_clients()

elif choice == "3":
    name = input ("Provied the client name to search")
    clients.search_client(name)

elif choice == "4":
    name = input ("Provies the client name to delete")
    clients.delete

elif choice == "5":
    print("You've added a new client !")

else: 
    print("I'm sorry, that is not an allowed action.")

if __name__ == "__main__":
    main()
