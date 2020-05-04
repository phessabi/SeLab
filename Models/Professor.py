from Models.Person import Person


class Professor(Person):
    def __init__(self, id_number: int, name: str):
        super(Professor, self).__init__(id_number, name)
