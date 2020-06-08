class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class Prueba:
    def __init__(self):
        self._contacts = []
        contacto = Contact("Carlos", "3345453","paco@gmail.com")
        self._contacts.append(contacto)
        contacto2 = Contact("Daniel", "3355453","memo@gmail.com")
        self._contacts.append(contacto2)
        
        print(self._contacts)

        for i in self._contacts:
            print(contacto.name)
            print(contacto.email)
            print(contacto.phone)

        for idx, j in enumerate(self._contacts):
            print(idx)
            print(j)
            print(j.name)

def run():
    Prueba()


if __name__ == '__main__':
    run()

