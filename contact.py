def deserialize(data):
    return Contact(data[0], data[1], data[2], data[3], data[4])


class Contact:

    def __init__(self, first_name, last_name, mail, phone, middle_name=""):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.mail = mail
        self.phone = phone

    def __repr__(self):
        return "\n".join(
            ["First Name:   " + self.first_name, "Middle Name:  " + self.middle_name, "Last Name:    " + self.last_name,
             "Mail Address: " + self.mail, "Phone Number: " + self.phone])

    def serialize(self):
        return ";".join([self.first_name, self.last_name, self.mail, self.phone, self.middle_name])
