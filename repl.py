from contact import Contact
from storage import Storage


class Repl:

    def __init__(self):
        self.storage = Storage()
        self.print_help()
        self.start()

    def start(self):
        while True:
            user_input = input()
            attributes = user_input.split(" ")
            command = attributes[0]
            attributes = attributes[1:]
            self.do_command(command, attributes)

    def print_help(self):
        print("--------------------------USAGE---------------------------")
        print("HELP                         - shows this page")
        print("QUIT                         - terminates this process")
        print("ADD                          - adds a new contact")
        print("LIST                         - shows all known contacts")
        print("SHOW <firstName> <lastName>  - shows an existing contact")
        print("DEL  <firstName> <lastName>  - removes an existing contact")
        print("EDIT <firstName> <lastName>  - edits an existing contact")
        print("----------------------------------------------------------\n")

    def do_command(self, command, attributes):
        if command == "QUIT":
            quit()
        if command == "HELP":
            self.print_help()
        if command == "ADD":
            self.add_contact_repl()
        if command == "LIST":
            self.list_contacts_repl()
        if command == "SHOW":
            self.show_contact_repl(attributes)
        if command == "DEL":
            self.del_contact_repl(attributes)
        if command == "EDIT":
            self.edit_contact_repl(attributes)

    def add_contact_repl(self):
        print("First Name:")
        first_name = input()
        print("Last Name:")
        last_name = input()
        print("Middle Name:")
        middle_name = input()
        print("Mail Address:")
        mail = input()
        print("Phone Number:")
        phone = input()
        contact = Contact(first_name, last_name, phone, mail, middle_name)
        self.storage.save(contact)
        print("Saved")

    def show_contact_repl(self, attributes):
        if self.check_attributes(attributes, 2):
            return
        contact = self.storage.load(attributes[0], attributes[1])
        if contact is None:
            print("contact is not present")
        else:
            print(contact)

    def list_contacts_repl(self):
        for name in self.storage.list_all():
            print(name)

    def del_contact_repl(self, attributes):
        if self.check_attributes(attributes, 2):
            return
        was_deleted = self.storage.delete(attributes[0], attributes[1])
        if was_deleted:
            print("Deleted contact " + attributes[0] + " " + attributes[1])
        else:
            print("Deleted no contact")

    def edit_contact_repl(self, attributes):
        if self.check_attributes(attributes, 2):
            return
        contact = self.storage.load(attributes[0], attributes[1])
        if contact is None:
            print("contact is not present")
        else:
            self.storage.delete(contact.first_name, contact.last_name)
            self.add_contact_repl()

    def check_attributes(self, attributes, length):
        if len(attributes) < length:
            self.print_help()
            return True
        return False
