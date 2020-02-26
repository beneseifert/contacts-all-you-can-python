import io
import os
from contact import Contact, deserialize

STORAGE_FOLDER = "./contacts/"


class Storage:

    def __init__(self):
        pass

    def create_file_name(self, first_name, last_name):
        return STORAGE_FOLDER + first_name + last_name + ".txt"

    def save(self, contact):
        file_name = self.create_file_name(contact.first_name, contact.last_name)
        with io.open(file_name, "w", encoding="utf-8") as f:
            f.write(contact.serialize())

    def load(self, first_name, last_name):
        file_name = self.create_file_name(first_name, last_name)
        with io.open(file_name, "r", encoding="utf-8") as f:
            try:
                serialized_contact = f.read()
                contact = deserialize(serialized_contact.split(";"))
                return contact
            except FileNotFoundError:
                return None

    def delete(self, first_name, last_name):
        file_name = self.create_file_name(first_name, last_name)
        try:
            os.remove(file_name)
            return True
        except OSError:
            return False

    def list_all(self):
        names = []
        files = os.listdir(STORAGE_FOLDER)
        for file in files:
            with io.open(STORAGE_FOLDER + file, "r", encoding="utf-8") as f:
                try:
                    serialized_contact = f.read()
                    contact = deserialize(serialized_contact.split(";"))
                    names.append(contact.first_name + " " + contact.last_name)
                except FileNotFoundError:
                    pass
        return sorted(names)
