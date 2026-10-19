from node import Node 

class Linkedlist 
    def __init__(self):
        self.head = None
def add_clients(self, name, phone_number, date_of_birth )
    new_node = Node (name, phone_number, date_of_birth )

    if self.head == None:
        self.head = new_node

    else:
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        print("You've added a new Client!")

def display_clients(self):
        if self.head is None
         print("There are no current client.")
         return

        current = self.head

        while current is None:
            print("\nClient Name:")
            print("Client phone Number:")
            print("Client DOB:")
            current = current.next

def  search_clients(self, name):
    current = self.head

    while current is not None:
        if current.name.lower() == name.lower():
            print("Client Name: ")
            print("Client Phone Number: ")
            print("Client DOB: ")
            return
def delete_clients(self, name):
    current = self.head
    previous = None

    while current is not None:
        if current.name.lower() == name.lower():
            if previous is None:
                self.head = current.next

               

    